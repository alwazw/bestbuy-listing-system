# Deployment Guide - Best Buy Listing System

Complete step-by-step deployment instructions for setting up the Best Buy Listing System in any environment.

## 🎯 Deployment Overview

This guide covers multiple deployment scenarios:
- **Local Development**: Quick setup for development and testing
- **Production Server**: Full production deployment on Ubuntu/Linux
- **Docker Deployment**: Containerized deployment (coming soon)
- **Cloud Deployment**: AWS/Azure/GCP deployment options

## 📋 Prerequisites

### System Requirements
- **Operating System**: Ubuntu 20.04+ (recommended) or any Linux distribution
- **Python**: 3.11 or higher
- **Node.js**: 20.0 or higher
- **Memory**: Minimum 2GB RAM (4GB recommended)
- **Storage**: 1GB free space
- **Network**: Internet access for package installation

### Required Software
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python 3.11 and pip
sudo apt install python3.11 python3.11-pip python3.11-venv -y

# Install Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Git
sudo apt install git -y

# Verify installations
python3.11 --version  # Should show Python 3.11.x
node --version        # Should show v20.x.x
npm --version         # Should show 10.x.x
git --version         # Should show git version
```

## 🚀 Quick Deployment (5 Minutes)

### Step 1: Clone Repository
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/bestbuy-listing-system.git
cd bestbuy-listing-system
```

### Step 2: Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create Python virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install flask flask-cors pandas openpyxl requests beautifulsoup4

# Start the backend server
python bestbuy_api.py
```
✅ Backend will be running at `http://localhost:5000`

### Step 3: Frontend Setup (New Terminal)
```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install Node.js dependencies
npm install

# Start the development server
npm run dev
```
✅ Frontend will be running at `http://localhost:5173`

### Step 4: Verify Installation
1. Open browser to `http://localhost:5173`
2. You should see the Best Buy Listing System interface
3. Test by filling in a sample product and generating a template

## 🔧 Detailed Production Deployment

### Step 1: Server Preparation
```bash
# Create dedicated user for the application
sudo useradd -m -s /bin/bash bestbuy
sudo usermod -aG sudo bestbuy

# Switch to application user
sudo su - bestbuy

# Create application directory
mkdir -p /home/bestbuy/apps
cd /home/bestbuy/apps
```

### Step 2: Application Setup
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/bestbuy-listing-system.git
cd bestbuy-listing-system

# Set proper permissions
chmod +x scripts/*.sh
```

### Step 3: Backend Production Setup
```bash
cd backend

# Create production virtual environment
python3.11 -m venv prod_venv
source prod_venv/bin/activate

# Install production dependencies
pip install --upgrade pip
pip install flask flask-cors pandas openpyxl requests beautifulsoup4 gunicorn

# Create production configuration
cat > config.py << EOF
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    FLASK_ENV = 'production'
    DEBUG = False
    CORS_ORIGINS = ['http://localhost:3000', 'https://yourdomain.com']

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'
    CORS_ORIGINS = ['http://localhost:5173', 'http://localhost:3000']

class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'
EOF

# Create production startup script
cat > start_production.sh << 'EOF'
#!/bin/bash
source prod_venv/bin/activate
export FLASK_ENV=production
export SECRET_KEY="your-production-secret-key"
gunicorn --bind 0.0.0.0:5000 --workers 4 bestbuy_api:app
EOF

chmod +x start_production.sh
```

### Step 4: Frontend Production Build
```bash
cd ../frontend

# Install dependencies
npm install

# Create production build
npm run build

# Install serve for production serving
npm install -g serve

# Create production startup script
cat > start_frontend.sh << 'EOF'
#!/bin/bash
serve -s dist -l 3000
EOF

chmod +x start_frontend.sh
```

### Step 5: System Service Setup (Optional)
```bash
# Create systemd service for backend
sudo tee /etc/systemd/system/bestbuy-backend.service > /dev/null << EOF
[Unit]
Description=Best Buy Listing System Backend
After=network.target

[Service]
Type=simple
User=bestbuy
WorkingDirectory=/home/bestbuy/apps/bestbuy-listing-system/backend
ExecStart=/home/bestbuy/apps/bestbuy-listing-system/backend/start_production.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Create systemd service for frontend
sudo tee /etc/systemd/system/bestbuy-frontend.service > /dev/null << EOF
[Unit]
Description=Best Buy Listing System Frontend
After=network.target

[Service]
Type=simple
User=bestbuy
WorkingDirectory=/home/bestbuy/apps/bestbuy-listing-system/frontend
ExecStart=/home/bestbuy/apps/bestbuy-listing-system/frontend/start_frontend.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Enable and start services
sudo systemctl daemon-reload
sudo systemctl enable bestbuy-backend bestbuy-frontend
sudo systemctl start bestbuy-backend bestbuy-frontend

# Check service status
sudo systemctl status bestbuy-backend
sudo systemctl status bestbuy-frontend
```

## 🌐 Nginx Reverse Proxy Setup (Recommended)

### Install and Configure Nginx
```bash
# Install Nginx
sudo apt install nginx -y

# Create Nginx configuration
sudo tee /etc/nginx/sites-available/bestbuy-listing-system > /dev/null << 'EOF'
server {
    listen 80;
    server_name your-domain.com;  # Replace with your domain

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}
EOF

# Enable the site
sudo ln -s /etc/nginx/sites-available/bestbuy-listing-system /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 🔒 SSL/HTTPS Setup with Let's Encrypt
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain SSL certificate
sudo certbot --nginx -d your-domain.com

# Verify auto-renewal
sudo certbot renew --dry-run
```

## 🐳 Docker Deployment (Alternative)

### Create Dockerfile for Backend
```dockerfile
# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "bestbuy_api:app"]
```

### Create Dockerfile for Frontend
```dockerfile
# frontend/Dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
```

### Docker Compose Setup
```yaml
# docker-compose.yml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    volumes:
      - ./templates:/app/templates

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  nginx:
    image: nginx:alpine
    ports:
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - frontend
      - backend
```

## 🔧 Environment Configuration

### Backend Environment Variables
```bash
# Create .env file in backend directory
cat > backend/.env << EOF
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
DEBUG=False
CORS_ORIGINS=https://yourdomain.com,http://localhost:3000
UPLOAD_FOLDER=/tmp/uploads
MAX_CONTENT_LENGTH=16777216
EOF
```

### Frontend Environment Variables
```bash
# Create .env file in frontend directory
cat > frontend/.env << EOF
VITE_API_BASE_URL=https://yourdomain.com/api
VITE_APP_TITLE=Best Buy Listing System
VITE_APP_VERSION=1.0.0
EOF
```

## 📊 Monitoring and Logging

### Setup Application Logging
```bash
# Create log directory
sudo mkdir -p /var/log/bestbuy-listing-system
sudo chown bestbuy:bestbuy /var/log/bestbuy-listing-system

# Configure log rotation
sudo tee /etc/logrotate.d/bestbuy-listing-system > /dev/null << EOF
/var/log/bestbuy-listing-system/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 644 bestbuy bestbuy
}
EOF
```

### Health Check Endpoints
The system includes health check endpoints:
- Backend: `http://localhost:5000/health`
- Frontend: `http://localhost:3000/health`

## 🔄 Backup and Recovery

### Automated Backup Script
```bash
#!/bin/bash
# backup.sh

BACKUP_DIR="/home/bestbuy/backups"
DATE=$(date +%Y%m%d_%H%M%S)
APP_DIR="/home/bestbuy/apps/bestbuy-listing-system"

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup application files
tar -czf $BACKUP_DIR/bestbuy-app-$DATE.tar.gz -C $APP_DIR .

# Backup templates
cp -r $APP_DIR/templates $BACKUP_DIR/templates-$DATE

# Keep only last 30 days of backups
find $BACKUP_DIR -name "*.tar.gz" -mtime +30 -delete
find $BACKUP_DIR -name "templates-*" -mtime +30 -exec rm -rf {} \;

echo "Backup completed: $DATE"
```

### Recovery Procedure
```bash
# Stop services
sudo systemctl stop bestbuy-backend bestbuy-frontend

# Restore from backup
cd /home/bestbuy/apps
tar -xzf /home/bestbuy/backups/bestbuy-app-YYYYMMDD_HHMMSS.tar.gz

# Restart services
sudo systemctl start bestbuy-backend bestbuy-frontend
```

## 🧪 Testing Deployment

### Automated Testing Script
```bash
#!/bin/bash
# test_deployment.sh

echo "Testing Best Buy Listing System Deployment..."

# Test backend health
echo "Testing backend..."
curl -f http://localhost:5000/health || exit 1

# Test frontend
echo "Testing frontend..."
curl -f http://localhost:3000 || exit 1

# Test API endpoints
echo "Testing API endpoints..."
curl -f http://localhost:5000/api/categories || exit 1

echo "All tests passed! ✅"
```

## 🚨 Troubleshooting

### Common Issues and Solutions

**Backend won't start**
```bash
# Check Python version
python3.11 --version

# Check virtual environment
source backend/venv/bin/activate
pip list

# Check logs
journalctl -u bestbuy-backend -f
```

**Frontend build fails**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Permission issues**
```bash
# Fix ownership
sudo chown -R bestbuy:bestbuy /home/bestbuy/apps/bestbuy-listing-system

# Fix permissions
chmod +x scripts/*.sh
chmod +x backend/start_production.sh
chmod +x frontend/start_frontend.sh
```

**Port conflicts**
```bash
# Check what's using the ports
sudo netstat -tulpn | grep :5000
sudo netstat -tulpn | grep :3000

# Kill conflicting processes
sudo kill -9 $(sudo lsof -t -i:5000)
sudo kill -9 $(sudo lsof -t -i:3000)
```

## 📞 Support

For deployment issues:
1. Check the logs: `journalctl -u bestbuy-backend -f`
2. Verify all dependencies are installed
3. Ensure proper file permissions
4. Check firewall settings
5. Verify environment variables

## 🎉 Post-Deployment Checklist

- [ ] Backend API responding at `/health`
- [ ] Frontend loading correctly
- [ ] Template generation working
- [ ] File uploads functioning
- [ ] SSL certificate installed (production)
- [ ] Monitoring configured
- [ ] Backups scheduled
- [ ] Firewall configured
- [ ] DNS pointing to server (production)
- [ ] Performance testing completed

---

**Deployment Guide Version**: 1.0.0  
**Last Updated**: January 9, 2025  
**Tested On**: Ubuntu 22.04 LTS

