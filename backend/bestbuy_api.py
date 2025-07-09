#!/usr/bin/env python3
"""
Best Buy Listing API v1.0
Flask API for integrating with React frontend
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import json
from datetime import datetime
import logging
from pathlib import Path

# Import our Best Buy system
from bestbuy_template_generator import BestBuyListingManager, BestBuyFieldValidator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Initialize Best Buy system
listing_manager = BestBuyListingManager()
validator = BestBuyFieldValidator()

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0'
    })

@app.route('/api/validate', methods=['POST'])
def validate_listing():
    """Validate listing data without generating template"""
    try:
        form_data = request.get_json()
        
        if not form_data:
            return jsonify({
                'success': False,
                'message': 'No data provided'
            }), 400
        
        # Validate the data
        validation_result = listing_manager.validate_listing_data(form_data)
        
        return jsonify({
            'success': True,
            'validation': validation_result
        })
        
    except Exception as e:
        logger.error(f"Validation error: {e}")
        return jsonify({
            'success': False,
            'message': f'Validation error: {str(e)}'
        }), 500

@app.route('/api/generate-template', methods=['POST'])
def generate_template():
    """Generate Best Buy template from form data"""
    try:
        form_data = request.get_json()
        
        if not form_data:
            return jsonify({
                'success': False,
                'message': 'No data provided'
            }), 400
        
        # Generate template
        result = listing_manager.create_listing(form_data)
        
        if result['success']:
            return jsonify({
                'success': True,
                'message': result['message'],
                'file_path': result['file_path'],
                'summary': result['data_summary']
            })
        else:
            return jsonify({
                'success': False,
                'message': result['message'],
                'errors': result.get('errors', {})
            }), 400
            
    except Exception as e:
        logger.error(f"Template generation error: {e}")
        return jsonify({
            'success': False,
            'message': f'Template generation error: {str(e)}'
        }), 500

@app.route('/api/download-template/<filename>', methods=['GET'])
def download_template(filename):
    """Download generated template file"""
    try:
        file_path = f"/home/ubuntu/{filename}"
        
        if not os.path.exists(file_path):
            return jsonify({
                'success': False,
                'message': 'File not found'
            }), 404
        
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
    except Exception as e:
        logger.error(f"Download error: {e}")
        return jsonify({
            'success': False,
            'message': f'Download error: {str(e)}'
        }), 500

@app.route('/api/hierarchy-codes', methods=['GET'])
def get_hierarchy_codes():
    """Get available hierarchy codes"""
    try:
        hierarchy_codes = validator.hierarchy_codes
        
        # Format for frontend dropdown
        formatted_codes = []
        for code in hierarchy_codes[:20]:  # Limit to first 20 for demo
            if code.startswith('BB_'):
                # Try to get friendly name (this would be enhanced with actual mapping)
                friendly_name = {
                    'BB_36711': 'Windows Laptops',
                    'BB_36712': 'Gaming Laptops',
                    'BB_12746017': 'Apple MacBook Air',
                    'BB_12746018': 'Apple MacBook Pro'
                }.get(code, f'Category {code}')
                
                formatted_codes.append({
                    'value': code,
                    'label': f'{friendly_name} ({code})'
                })
        
        return jsonify({
            'success': True,
            'codes': formatted_codes
        })
        
    except Exception as e:
        logger.error(f"Hierarchy codes error: {e}")
        return jsonify({
            'success': False,
            'message': f'Error loading hierarchy codes: {str(e)}'
        }), 500

@app.route('/api/generate-sku', methods=['POST'])
def generate_sku():
    """Generate SKU from product information"""
    try:
        data = request.get_json()
        
        brand = data.get('brand_name', '').strip()
        model = data.get('model_number', '').strip()
        memory = data.get('memory_size', '').strip()
        storage = data.get('storage_capacity', '').strip()
        
        if not all([brand, model]):
            return jsonify({
                'success': False,
                'message': 'Brand and model are required for SKU generation'
            }), 400
        
        # Generate SKU components
        brand_abbrev = brand[:2].upper() if brand else 'XX'
        model_abbrev = 'i7' if 'i7' in model.lower() else 'i5' if 'i5' in model.lower() else model[:2].upper()
        memory_val = memory if memory else '16'
        storage_val = storage if storage else '512'
        
        generated_sku = f"{brand_abbrev}-{model_abbrev}-{memory_val}-{storage_val}"
        
        return jsonify({
            'success': True,
            'sku': generated_sku
        })
        
    except Exception as e:
        logger.error(f"SKU generation error: {e}")
        return jsonify({
            'success': False,
            'message': f'SKU generation error: {str(e)}'
        }), 500

@app.route('/api/field-info', methods=['GET'])
def get_field_info():
    """Get field information and validation rules"""
    try:
        # Load field mappings
        field_mappings_path = '/home/ubuntu/bestbuy_field_mappings.json'
        if os.path.exists(field_mappings_path):
            with open(field_mappings_path, 'r') as f:
                field_mappings = json.load(f)
        else:
            field_mappings = []
        
        # Load validation rules
        validation_rules_path = '/home/ubuntu/bestbuy_validation_rules.json'
        if os.path.exists(validation_rules_path):
            with open(validation_rules_path, 'r') as f:
                validation_rules = json.load(f)
        else:
            validation_rules = {}
        
        return jsonify({
            'success': True,
            'field_mappings': field_mappings,
            'validation_rules': validation_rules
        })
        
    except Exception as e:
        logger.error(f"Field info error: {e}")
        return jsonify({
            'success': False,
            'message': f'Error loading field information: {str(e)}'
        }), 500

@app.route('/api/templates', methods=['GET'])
def list_templates():
    """List generated template files"""
    try:
        template_dir = Path('/home/ubuntu')
        template_files = list(template_dir.glob('bestbuy_listing_*.xlsx'))
        
        templates = []
        for file_path in template_files:
            stat = file_path.stat()
            templates.append({
                'filename': file_path.name,
                'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
                'size': stat.st_size
            })
        
        # Sort by creation time, newest first
        templates.sort(key=lambda x: x['created'], reverse=True)
        
        return jsonify({
            'success': True,
            'templates': templates
        })
        
    except Exception as e:
        logger.error(f"Template listing error: {e}")
        return jsonify({
            'success': False,
            'message': f'Error listing templates: {str(e)}'
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'message': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'message': 'Internal server error'
    }), 500

if __name__ == '__main__':
    print("Starting Best Buy Listing API...")
    print("Available endpoints:")
    print("  GET  /api/health - Health check")
    print("  POST /api/validate - Validate listing data")
    print("  POST /api/generate-template - Generate Best Buy template")
    print("  GET  /api/download-template/<filename> - Download template")
    print("  GET  /api/hierarchy-codes - Get hierarchy codes")
    print("  POST /api/generate-sku - Generate SKU")
    print("  GET  /api/field-info - Get field information")
    print("  GET  /api/templates - List generated templates")
    print()
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)

