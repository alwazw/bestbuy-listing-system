#!/bin/bash

# Best Buy Listing System - Automated Deployment Script
# This script automates the complete deployment process

set -e  # Exit on any error

echo "🚀 Best Buy Listing System - Automated Deployment"
echo "=================================================="

# Configuration
PROJECT_NAME="bestbuy-listing-system"
BACKEND_PORT=5000
FRONTEND_PORT=3000
PYTHON_VERSION="3.11"
NODE_VERSION="20"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running as root
check_root() {
    if [[ $EUID -eq 0 ]]; then
        log_error "This script should not be run as root"
        exit 1
    fi
}

# Check system requirements
check_requirements() {
    log_info "Checking system requirements..."
    
    # Check Python
    if ! command -v python3.11 &> /dev/null; then
        log_error "Python 3.11 is required but not installed"
        log_info "Install with: sudo apt install python3.11 python3.11-pip python3.11-venv"
        exit 1
    fi
    
    # Check Node.js
    if ! command -v node &> /dev/null; then
        log_error "Node.js is required but not installed"
        log_info "Install with: curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt-get install -y nodejs"
        exit 1
    fi
    
    # Check npm
    if ! command -v npm &> /dev/null; then
        log_error "npm is required but not installed"
        exit 1
    fi
    
    log_success "All requirements satisfied"
}

# Setup backend
setup_backend() {
    log_info "Setting up backend..."
    
    cd backend
    
    # Create virtual environment
    if [ ! -d "venv" ]; then
        log_info "Creating Python virtual environment..."
        python3.11 -m venv venv
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Upgrade pip
    pip install --upgrade pip
    
    # Install dependencies
    log_info "Installing Python dependencies..."
    pip install -r requirements.txt
    
    # Create .env file if it doesn't exist
    if [ ! -f ".env" ]; then
        log_info "Creating backend .env file..."
        cat > .env << EOF
FLASK_ENV=development
SECRET_KEY=dev-secret-key-change-in-production
DEBUG=True
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
UPLOAD_FOLDER=./uploads
MAX_CONTENT_LENGTH=16777216
EOF
    fi
    
    # Create uploads directory
    mkdir -p uploads
    
    cd ..
    log_success "Backend setup completed"
}

# Setup frontend
setup_frontend() {
    log_info "Setting up frontend..."
    
    cd frontend
    
    # Install dependencies
    log_info "Installing Node.js dependencies..."
    npm install
    
    # Create .env file if it doesn't exist
    if [ ! -f ".env" ]; then
        log_info "Creating frontend .env file..."
        cat > .env << EOF
VITE_API_BASE_URL=http://localhost:5000
VITE_APP_TITLE=Best Buy Listing System
VITE_APP_VERSION=1.0.0
EOF
    fi
    
    cd ..
    log_success "Frontend setup completed"
}

# Create startup scripts
create_startup_scripts() {
    log_info "Creating startup scripts..."
    
    # Backend startup script
    cat > start_backend.sh << 'EOF'
#!/bin/bash
cd backend
source venv/bin/activate
export FLASK_ENV=development
python bestbuy_api.py
EOF
    
    # Frontend startup script
    cat > start_frontend.sh << 'EOF'
#!/bin/bash
cd frontend
npm run dev
EOF
    
    # Production startup script
    cat > start_production.sh << 'EOF'
#!/bin/bash

# Start backend in background
cd backend
source venv/bin/activate
export FLASK_ENV=production
export SECRET_KEY="change-this-in-production"
gunicorn --bind 0.0.0.0:5000 --workers 4 --daemon bestbuy_api:app

# Build and serve frontend
cd ../frontend
npm run build
serve -s dist -l 3000 &

echo "Production servers started:"
echo "Frontend: http://localhost:3000"
echo "Backend: http://localhost:5000"
EOF
    
    # Make scripts executable
    chmod +x start_backend.sh start_frontend.sh start_production.sh
    
    log_success "Startup scripts created"
}

# Test deployment
test_deployment() {
    log_info "Testing deployment..."
    
    # Start backend in background
    cd backend
    source venv/bin/activate
    python bestbuy_api.py &
    BACKEND_PID=$!
    cd ..
    
    # Wait for backend to start
    sleep 5
    
    # Test backend health
    if curl -f http://localhost:5000/health > /dev/null 2>&1; then
        log_success "Backend is responding"
    else
        log_error "Backend health check failed"
        kill $BACKEND_PID 2>/dev/null || true
        exit 1
    fi
    
    # Stop backend
    kill $BACKEND_PID 2>/dev/null || true
    
    log_success "Deployment test completed"
}

# Main deployment function
main() {
    log_info "Starting deployment process..."
    
    check_root
    check_requirements
    setup_backend
    setup_frontend
    create_startup_scripts
    test_deployment
    
    log_success "Deployment completed successfully!"
    echo ""
    echo "🎉 Best Buy Listing System is ready!"
    echo ""
    echo "To start the system:"
    echo "  Development mode:"
    echo "    Backend:  ./start_backend.sh"
    echo "    Frontend: ./start_frontend.sh"
    echo ""
    echo "  Production mode:"
    echo "    ./start_production.sh"
    echo ""
    echo "Access the application at:"
    echo "  Frontend: http://localhost:3000 (production) or http://localhost:5173 (development)"
    echo "  Backend:  http://localhost:5000"
    echo ""
    echo "Documentation available in docs/ directory"
}

# Run main function
main "$@"

