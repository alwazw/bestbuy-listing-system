import pandas as pd
import json

def create_bestbuy_field_mappings():
    """Create comprehensive Best Buy field mappings from template analysis"""
    
    # Read the columns reference sheet
    columns_df = pd.read_excel('/home/ubuntu/upload/AS-i7-Export.xlsx', sheet_name='Columns')
    
    # Create comprehensive field mapping
    field_mappings = []
    
    for index, row in columns_df.iterrows():
        field_info = {
            'field_code': row['Code'],
            'field_label': row['Label'],
            'description': row['Description'] if pd.notna(row['Description']) else '',
            'example_value': row['Value example'] if pd.notna(row['Value example']) else '',
            'requirement_level': row['Computers/Laptops'] if pd.notna(row['Computers/Laptops']) else 'OPTIONAL',
            'character_limit': None,  # Will be extracted from description
            'validation_rules': [],
            'field_type': 'text',  # Default, will be refined
            'category': 'general'  # Will be categorized
        }
        
        # Extract character limits from description
        description = str(field_info['description']).lower()
        if 'character' in description:
            import re
            char_match = re.search(r'(\d+)\s*character', description)
            if char_match:
                field_info['character_limit'] = int(char_match.group(1))
        
        # Categorize fields
        field_code = str(field_info['field_code']).lower()
        if any(x in field_code for x in ['title', 'description', 'brand', 'model']):
            field_info['category'] = 'core_product_info'
        elif any(x in field_code for x in ['price', 'cost', 'msrp']):
            field_info['category'] = 'pricing'
        elif any(x in field_code for x in ['image', 'photo', 'picture']):
            field_info['category'] = 'media'
        elif any(x in field_code for x in ['processor', 'memory', 'storage', 'display', 'screen']):
            field_info['category'] = 'technical_specs'
        elif any(x in field_code for x in ['dimension', 'weight', 'size']):
            field_info['category'] = 'physical_specs'
        elif any(x in field_code for x in ['shipping', 'fulfillment', 'delivery']):
            field_info['category'] = 'logistics'
        elif any(x in field_code for x in ['warranty', 'support', 'service']):
            field_info['category'] = 'support'
        
        # Determine field type
        if 'yes/no' in description or 'boolean' in description:
            field_info['field_type'] = 'boolean'
        elif any(x in description for x in ['price', 'cost', 'amount', 'currency']):
            field_info['field_type'] = 'currency'
        elif any(x in description for x in ['number', 'quantity', 'count']):
            field_info['field_type'] = 'number'
        elif any(x in description for x in ['date', 'time']):
            field_info['field_type'] = 'datetime'
        elif any(x in description for x in ['url', 'link', 'http']):
            field_info['field_type'] = 'url'
        elif 'select' in description or 'choose' in description:
            field_info['field_type'] = 'select'
        
        field_mappings.append(field_info)
    
    return field_mappings

def generate_field_reference_document(field_mappings):
    """Generate a comprehensive field reference document"""
    
    # Group fields by category
    categories = {}
    for field in field_mappings:
        category = field['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(field)
    
    # Generate markdown document
    doc_content = """# Best Buy Field Reference Guide

**Generated:** January 7, 2025  
**Total Fields:** {}  

## Field Categories Overview

""".format(len(field_mappings))
    
    # Add category summary
    for category, fields in categories.items():
        required_count = len([f for f in fields if f['requirement_level'] == 'REQUIRED'])
        recommended_count = len([f for f in fields if f['requirement_level'] == 'RECOMMENDED'])
        optional_count = len([f for f in fields if f['requirement_level'] == 'OPTIONAL'])
        
        doc_content += f"- **{category.replace('_', ' ').title()}:** {len(fields)} fields ({required_count} required, {recommended_count} recommended, {optional_count} optional)\n"
    
    doc_content += "\n## Detailed Field Specifications\n\n"
    
    # Add detailed field information by category
    for category, fields in categories.items():
        doc_content += f"### {category.replace('_', ' ').title()}\n\n"
        
        # Create table for this category
        doc_content += "| Field Code | Label | Type | Required | Char Limit | Description |\n"
        doc_content += "|------------|-------|------|----------|------------|-------------|\n"
        
        for field in sorted(fields, key=lambda x: x['requirement_level']):
            char_limit = str(field['character_limit']) if field['character_limit'] else 'N/A'
            description = field['description'][:100] + '...' if len(field['description']) > 100 else field['description']
            description = description.replace('\n', ' ').replace('|', '\\|')
            
            doc_content += f"| {field['field_code']} | {field['field_label']} | {field['field_type']} | {field['requirement_level']} | {char_limit} | {description} |\n"
        
        doc_content += "\n"
    
    return doc_content

def create_validation_rules():
    """Create validation rules for Best Buy fields"""
    
    validation_rules = {
        'BBYCat': {
            'required': True,
            'type': 'select',
            'validation': 'must_match_hierarchy_codes',
            'error_message': 'Category code must match valid Best Buy hierarchy code'
        },
        'shop_sku': {
            'required': True,
            'type': 'text',
            'max_length': 30,
            'pattern': r'^[A-Z0-9\-]+$',
            'unique': True,
            'validation': 'sku_format_check',
            'error_message': 'SKU must be unique, max 30 chars, alphanumeric with hyphens only'
        },
        '_Title_BB_Category_Root_EN': {
            'required': True,
            'type': 'text',
            'max_length': 180,
            'validation': 'title_condition_suffix_check',
            'prohibited_chars': ['#', '[', ']', '😀', ';'],
            'error_message': 'Title must end with condition, max 180 chars, no special characters'
        },
        '_Short_Description_BB_Category_Root_EN': {
            'required': True,
            'type': 'text',
            'max_length': 480,
            'validation': 'no_external_references',
            'prohibited_content': ['http', 'www.', 'amazon', 'walmart'],
            'error_message': 'Short description max 480 chars, no external references or HTML'
        },
        '_Brand_Name_Category_Root_EN': {
            'required': True,
            'type': 'text',
            'max_length': 20,
            'validation': 'brand_name_only',
            'error_message': 'Brand name only, max 20 characters, not store name'
        },
        '_Model_Number_Category_Root_EN': {
            'required': True,
            'type': 'text',
            'max_length': 20,
            'validation': 'simplified_model_format',
            'error_message': 'Simplified model designation, max 20 characters'
        },
        '_Manufacturers_Part_Number_Category_Root_EN': {
            'required': True,
            'type': 'text',
            'max_length': 30,
            'validation': 'mpn_or_model_number',
            'error_message': 'MPN or model number if no MPN exists, max 30 characters'
        },
        '_Long_Description_Category_Root_EN': {
            'required': True,
            'type': 'text',
            'max_length': 10000,
            'validation': 'bullet_format_recommended',
            'prohibited_content': ['http', 'www.', 'amazon', 'walmart'],
            'error_message': 'Long description max 10,000 chars, bullet format recommended, no external links'
        },
        '_Product_Condition_Category_Root_EN': {
            'required': True,
            'type': 'select',
            'options': [
                'Brand New',
                'Open Box',
                'Refurbished (Excellent)',
                'Refurbished (Good)',
                'Refurbished (Fair)'
            ],
            'validation': 'predefined_values_only',
            'error_message': 'Must select from predefined condition values'
        },
        '_Web_Hierarchy_Location_Category_Root_EN': {
            'required': True,
            'type': 'select',
            'validation': 'must_match_hierarchy_codes',
            'error_message': 'Must match valid Best Buy web hierarchy location code'
        }
    }
    
    return validation_rules

# Execute the functions
if __name__ == "__main__":
    print("Creating Best Buy field mappings...")
    field_mappings = create_bestbuy_field_mappings()
    
    print("Generating field reference document...")
    doc_content = generate_field_reference_document(field_mappings)
    
    print("Creating validation rules...")
    validation_rules = create_validation_rules()
    
    # Save field mappings as JSON
    with open('/home/ubuntu/bestbuy_field_mappings.json', 'w') as f:
        json.dump(field_mappings, f, indent=2)
    
    # Save validation rules as JSON
    with open('/home/ubuntu/bestbuy_validation_rules.json', 'w') as f:
        json.dump(validation_rules, f, indent=2)
    
    # Save field reference document
    with open('/home/ubuntu/bestbuy_field_reference.md', 'w') as f:
        f.write(doc_content)
    
    print(f"Generated {len(field_mappings)} field mappings")
    print("Files created:")
    print("- bestbuy_field_mappings.json")
    print("- bestbuy_validation_rules.json") 
    print("- bestbuy_field_reference.md")

