# API Reference - Best Buy Listing System

Complete API documentation for the Best Buy Listing System backend.

## 🌐 Base URL

- **Development**: `http://localhost:5000`
- **Production**: `https://yourdomain.com/api`

## 🔐 Authentication

Currently, the API does not require authentication. All endpoints are publicly accessible.

## 📋 API Endpoints

### Health Check

#### GET /health
Check if the API server is running and healthy.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-01-09T15:37:07Z",
  "version": "1.0.0"
}
```

**Status Codes:**
- `200 OK`: Server is healthy
- `500 Internal Server Error`: Server issues

---

### Product Management

#### POST /api/generate-template
Generate a Best Buy template from product data.

**Request Body:**
```json
{
  "products": [
    {
      "brand": "Dell",
      "model": "Latitude 7390",
      "processor": "Intel Core i7-8650U",
      "memory": "32GB",
      "storage": "1TB SSD",
      "condition": "Refurbished (Excellent)",
      "screen_size": "13.3 inches",
      "touchscreen": false,
      "operating_system": "Windows 10 Pro"
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "filename": "bestbuy_template_20250109_153707.xlsx",
  "products_processed": 1,
  "download_url": "/api/download/bestbuy_template_20250109_153707.xlsx",
  "summary": {
    "total_products": 1,
    "successful": 1,
    "failed": 0,
    "validation_errors": []
  }
}
```

**Status Codes:**
- `200 OK`: Template generated successfully
- `400 Bad Request`: Invalid product data
- `422 Unprocessable Entity`: Validation errors
- `500 Internal Server Error`: Generation failed

---

#### POST /api/validate-product
Validate product data without generating template.

**Request Body:**
```json
{
  "brand": "Dell",
  "model": "Latitude 7390",
  "processor": "Intel Core i7-8650U",
  "memory": "32GB",
  "storage": "1TB SSD",
  "condition": "Refurbished (Excellent)"
}
```

**Response:**
```json
{
  "valid": true,
  "errors": [],
  "warnings": [],
  "suggestions": {
    "sku": "DL-7390-32-1000-RE",
    "title": "Dell Latitude 7390 13.3\" Full HD Business Laptop - Intel Core i7-8650U, 32GB DDR4, 1TB SSD, Windows 10 Pro - Refurbished (Excellent)",
    "category": "BB_36711"
  }
}
```

**Status Codes:**
- `200 OK`: Validation completed
- `400 Bad Request`: Invalid request format

---

#### POST /api/generate-sku
Generate SKU for a product.

**Request Body:**
```json
{
  "brand": "Dell",
  "model": "Latitude 7390",
  "memory": "32GB",
  "storage": "1TB",
  "condition": "Refurbished (Excellent)"
}
```

**Response:**
```json
{
  "sku": "DL-7390-32-1000-RE",
  "pattern": "Brand-Model-Memory-Storage-Condition",
  "components": {
    "brand_code": "DL",
    "model_code": "7390",
    "memory_code": "32",
    "storage_code": "1000",
    "condition_code": "RE"
  }
}
```

**Status Codes:**
- `200 OK`: SKU generated successfully
- `400 Bad Request`: Missing required fields

---

### Category Management

#### GET /api/categories
Get all available Best Buy categories.

**Response:**
```json
{
  "categories": [
    {
      "code": "BB_36711",
      "name": "Windows Laptops",
      "description": "Laptops running Windows operating system",
      "parent": "BB_36700"
    }
  ]
}
```

**Status Codes:**
- `200 OK`: Categories retrieved successfully

---

#### GET /api/categories/{code}
Get specific category details.

**Parameters:**
- `code` (string): Category code (e.g., "BB_36711")

**Response:**
```json
{
  "code": "BB_36711",
  "name": "Windows Laptops",
  "description": "Laptops running Windows operating system",
  "parent": "BB_36700",
  "required_fields": [
    "brand",
    "model",
    "processor",
    "memory",
    "storage",
    "screen_size",
    "operating_system"
  ],
  "optional_fields": [
    "graphics",
    "weight",
    "color",
    "warranty"
  ]
}
```

**Status Codes:**
- `200 OK`: Category found
- `404 Not Found`: Category not found

---

### File Management

#### GET /api/download/{filename}
Download generated template file.

**Parameters:**
- `filename` (string): Name of the file to download

**Response:**
- File download with appropriate headers

**Status Codes:**
- `200 OK`: File downloaded successfully
- `404 Not Found`: File not found

---

#### GET /api/templates
List all generated templates.

**Response:**
```json
{
  "templates": [
    {
      "filename": "bestbuy_template_20250109_153707.xlsx",
      "created_at": "2025-01-09T15:37:07Z",
      "size": 12518,
      "products_count": 1,
      "download_url": "/api/download/bestbuy_template_20250109_153707.xlsx"
    }
  ]
}
```

**Status Codes:**
- `200 OK`: Templates listed successfully

---

### Utility Endpoints

#### POST /api/enhance-description
Enhance product description using AI.

**Request Body:**
```json
{
  "product": {
    "brand": "Dell",
    "model": "Latitude 7390",
    "processor": "Intel Core i7-8650U",
    "memory": "32GB",
    "storage": "1TB SSD"
  },
  "description_type": "long"
}
```

**Response:**
```json
{
  "enhanced_description": "The Dell Latitude 7390 represents the ultimate in business mobility, combining premium performance with enterprise-grade security in an ultra-portable design...",
  "original_length": 0,
  "enhanced_length": 287,
  "improvements": [
    "Added professional tone",
    "Included technical specifications",
    "Emphasized business use cases"
  ]
}
```

**Status Codes:**
- `200 OK`: Description enhanced successfully
- `400 Bad Request`: Invalid product data

---

#### GET /api/field-mappings
Get all field mappings for Best Buy template.

**Response:**
```json
{
  "mappings": {
    "Shop sku": {
      "required": true,
      "type": "string",
      "max_length": 50,
      "description": "Unique SKU identifier"
    },
    "Title BB (EN)": {
      "required": true,
      "type": "string",
      "max_length": 200,
      "description": "Product title for Best Buy listing"
    }
  }
}
```

**Status Codes:**
- `200 OK`: Field mappings retrieved successfully

---

## 🔧 Request/Response Format

### Content Type
All requests and responses use `application/json` content type.

### Request Headers
```
Content-Type: application/json
Accept: application/json
```

### Response Headers
```
Content-Type: application/json
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Headers: Content-Type, Authorization
```

## ❌ Error Handling

### Error Response Format
```json
{
  "error": true,
  "message": "Detailed error message",
  "code": "ERROR_CODE",
  "details": {
    "field": "specific field that caused error",
    "value": "invalid value",
    "expected": "expected format or value"
  },
  "timestamp": "2025-01-09T15:37:07Z"
}
```

### Common Error Codes

| Code | Description |
|------|-------------|
| `VALIDATION_ERROR` | Product data validation failed |
| `MISSING_FIELD` | Required field is missing |
| `INVALID_FORMAT` | Field format is incorrect |
| `CATEGORY_NOT_FOUND` | Invalid category code |
| `FILE_NOT_FOUND` | Requested file doesn't exist |
| `GENERATION_FAILED` | Template generation failed |
| `INTERNAL_ERROR` | Server internal error |

## 📊 Rate Limiting

Currently, no rate limiting is implemented. In production, consider implementing:
- 100 requests per minute per IP
- 1000 template generations per hour per IP

## 🔍 Validation Rules

### Product Data Validation

#### Required Fields
- `brand`: String, 1-50 characters
- `model`: String, 1-100 characters
- `condition`: One of ["Brand New", "Open Box", "Refurbished (Excellent)", "Refurbished (Good)", "Refurbished (Fair)"]

#### Optional Fields
- `processor`: String, 1-100 characters
- `memory`: String with format "XGB" (e.g., "32GB")
- `storage`: String with format "XGB/TB SSD/HDD" (e.g., "1TB SSD")
- `screen_size`: String with format "X.X inches" (e.g., "13.3 inches")
- `touchscreen`: Boolean
- `operating_system`: String, 1-50 characters

#### SKU Format
- Pattern: `{BRAND_CODE}-{MODEL_CODE}-{MEMORY}-{STORAGE}-{CONDITION_CODE}`
- Example: `DL-7390-32-1000-RE`

#### Title Format
- Pattern: `{Brand} {Model} {Screen Size} {Key Features} - {Condition}`
- Max length: 200 characters
- Example: "Dell Latitude 7390 13.3\" Full HD Business Laptop - Intel Core i7-8650U, 32GB DDR4, 1TB SSD, Windows 10 Pro - Refurbished (Excellent)"

## 🧪 Testing

### Example cURL Commands

#### Generate Template
```bash
curl -X POST http://localhost:5000/api/generate-template \
  -H "Content-Type: application/json" \
  -d '{
    "products": [{
      "brand": "Dell",
      "model": "Latitude 7390",
      "processor": "Intel Core i7-8650U",
      "memory": "32GB",
      "storage": "1TB SSD",
      "condition": "Refurbished (Excellent)"
    }]
  }'
```

#### Validate Product
```bash
curl -X POST http://localhost:5000/api/validate-product \
  -H "Content-Type: application/json" \
  -d '{
    "brand": "Dell",
    "model": "Latitude 7390",
    "processor": "Intel Core i7-8650U",
    "memory": "32GB",
    "storage": "1TB SSD",
    "condition": "Refurbished (Excellent)"
  }'
```

#### Generate SKU
```bash
curl -X POST http://localhost:5000/api/generate-sku \
  -H "Content-Type: application/json" \
  -d '{
    "brand": "Dell",
    "model": "Latitude 7390",
    "memory": "32GB",
    "storage": "1TB",
    "condition": "Refurbished (Excellent)"
  }'
```

## 📝 Changelog

### Version 1.0.0 (2025-01-09)
- Initial API release
- Basic template generation
- Product validation
- SKU generation
- Category management
- File download functionality

---

**API Version**: 1.0.0  
**Last Updated**: January 9, 2025  
**Base URL**: `http://localhost:5000`

