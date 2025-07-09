#!/usr/bin/env python3
"""
Best Buy Listing Template Generator v1.0
Comprehensive system for validating, processing, and generating Best Buy marketplace listings
"""

import pandas as pd
import json
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BestBuyFieldValidator:
    """Comprehensive field validation for Best Buy listings"""
    
    def __init__(self):
        self.validation_rules = self._load_validation_rules()
        self.hierarchy_codes = self._load_hierarchy_codes()
        
    def _load_validation_rules(self) -> Dict:
        """Load validation rules from JSON file"""
        try:
            with open('/home/ubuntu/bestbuy_validation_rules.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning("Validation rules file not found, using default rules")
            return self._get_default_validation_rules()
    
    def _load_hierarchy_codes(self) -> List[str]:
        """Load valid hierarchy codes from Excel file"""
        try:
            df = pd.read_excel('/home/ubuntu/upload/WebHierarchyCodes-Dec2024.xlsx')
            # Filter for Web Leaf categories only (these are assignable)
            leaf_codes = df[df['<Object Type Name>'] == 'Web Leaf Best Buy']['<ID>'].dropna().tolist()
            return [str(code) for code in leaf_codes]
        except Exception as e:
            logger.error(f"Error loading hierarchy codes: {e}")
            return ['BB_36711', 'BB_36712']  # Default laptop categories
    
    def _get_default_validation_rules(self) -> Dict:
        """Default validation rules if file not found"""
        return {
            'shop_sku': {
                'required': True,
                'max_length': 30,
                'pattern': r'^[A-Z0-9\-]+$',
                'unique': True
            },
            '_Title_BB_Category_Root_EN': {
                'required': True,
                'max_length': 180,
                'validation': 'title_condition_suffix_check'
            },
            '_Brand_Name_Category_Root_EN': {
                'required': True,
                'max_length': 20
            }
        }
    
    def validate_field(self, field_code: str, value: Any, context: Dict = None) -> Tuple[bool, str]:
        """
        Validate a single field value
        
        Args:
            field_code: The field code to validate
            value: The value to validate
            context: Additional context for validation
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if field_code not in self.validation_rules:
            return True, ""
        
        rule = self.validation_rules[field_code]
        
        # Required field check
        if rule.get('required', False) and not self._has_value(value):
            return False, f"{field_code} is required"
        
        # Skip further validation if field is empty and not required
        if not self._has_value(value):
            return True, ""
        
        # String length validation
        if 'max_length' in rule and len(str(value)) > rule['max_length']:
            return False, f"{field_code} exceeds maximum length of {rule['max_length']} characters"
        
        # Pattern validation
        if 'pattern' in rule and not re.match(rule['pattern'], str(value)):
            return False, f"{field_code} does not match required format"
        
        # Custom validation functions
        if 'validation' in rule:
            return self._run_custom_validation(rule['validation'], field_code, value, context)
        
        return True, ""
    
    def _has_value(self, value: Any) -> bool:
        """Check if value is not empty"""
        if value is None:
            return False
        if isinstance(value, str):
            return bool(value.strip())
        return bool(value)
    
    def _run_custom_validation(self, validation_type: str, field_code: str, value: Any, context: Dict) -> Tuple[bool, str]:
        """Run custom validation functions"""
        
        if validation_type == 'title_condition_suffix_check':
            return self._validate_title_condition_suffix(value, context)
        elif validation_type == 'sku_format_check':
            return self._validate_sku_format(value)
        elif validation_type == 'must_match_hierarchy_codes':
            return self._validate_hierarchy_code(value)
        elif validation_type == 'no_external_references':
            return self._validate_no_external_references(value)
        elif validation_type == 'predefined_values_only':
            return self._validate_predefined_values(field_code, value)
        
        return True, ""
    
    def _validate_title_condition_suffix(self, title: str, context: Dict) -> Tuple[bool, str]:
        """Validate that title ends with proper condition suffix"""
        condition_options = [
            'Brand New',
            'Open Box',
            'Refurbished (Excellent)',
            'Refurbished (Good)',
            'Refurbished (Fair)'
        ]
        
        title_str = str(title).strip()
        
        # Check if title ends with any valid condition
        for condition in condition_options:
            if title_str.endswith(f" - {condition}"):
                return True, ""
        
        return False, f"Title must end with condition (e.g., ' - Refurbished (Excellent)')"
    
    def _validate_sku_format(self, sku: str) -> Tuple[bool, str]:
        """Validate SKU follows Brand-Model-Attribute-RAM-Storage format"""
        sku_str = str(sku).strip()
        parts = sku_str.split('-')
        
        if len(parts) < 3:
            return False, "SKU should follow format: Brand-Model-Attribute-RAM-Storage"
        
        # Check for valid characters
        if not re.match(r'^[A-Z0-9\-]+$', sku_str):
            return False, "SKU should contain only uppercase letters, numbers, and hyphens"
        
        return True, ""
    
    def _validate_hierarchy_code(self, code: str) -> Tuple[bool, str]:
        """Validate hierarchy code exists in valid codes list"""
        if str(code) not in self.hierarchy_codes:
            return False, f"Invalid hierarchy code. Must be one of the valid Best Buy category codes"
        return True, ""
    
    def _validate_no_external_references(self, text: str) -> Tuple[bool, str]:
        """Validate text contains no external references"""
        text_lower = str(text).lower()
        prohibited_terms = ['http', 'www.', 'amazon', 'walmart', 'ebay', '.com', '.ca']
        
        for term in prohibited_terms:
            if term in text_lower:
                return False, f"Text cannot contain external references or competitor names"
        
        return True, ""
    
    def _validate_predefined_values(self, field_code: str, value: str) -> Tuple[bool, str]:
        """Validate value is from predefined options"""
        predefined_values = {
            '_Product_Condition_Category_Root_EN': [
                'Brand New',
                'Open Box',
                'Refurbished (Excellent)',
                'Refurbished (Good)',
                'Refurbished (Fair)'
            ]
        }
        
        if field_code in predefined_values:
            if str(value) not in predefined_values[field_code]:
                return False, f"Value must be one of: {', '.join(predefined_values[field_code])}"
        
        return True, ""

class BestBuyDataProcessor:
    """Process and transform data for Best Buy template generation"""
    
    def __init__(self):
        self.validator = BestBuyFieldValidator()
        self.field_mappings = self._load_field_mappings()
    
    def _load_field_mappings(self) -> List[Dict]:
        """Load field mappings from JSON file"""
        try:
            with open('/home/ubuntu/bestbuy_field_mappings.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning("Field mappings file not found")
            return []
    
    def process_form_data(self, form_data: Dict) -> Dict:
        """
        Process form data and convert to Best Buy template format
        
        Args:
            form_data: Raw form data from frontend
            
        Returns:
            Processed data ready for template generation
        """
        processed_data = {}
        validation_errors = {}
        
        # Map form fields to Best Buy template fields
        field_mapping = {
            'shop_sku': 'shop_sku',
            'title': '_Title_BB_Category_Root_EN',
            'short_description': '_Short_Description_BB_Category_Root_EN',
            'long_description': '_Long_Description_Category_Root_EN',
            'brand_name': '_Brand_Name_Category_Root_EN',
            'model_number': '_Model_Number_Category_Root_EN',
            'mpn': '_Manufacturers_Part_Number_Category_Root_EN',
            'product_condition': '_Product_Condition_Category_Root_EN',
            'category_code': 'BBYCat',
            'web_hierarchy': '_Web_Hierarchy_Location_Category_Root_EN',
            'platform': '_Platform_Category_Root_EN',
            'variant_group': '_Variant_Group_Category_Root_EN',
            'processor_brand': '_Processor_Brand_Category_Root_EN',
            'processor_model': '_Processor_Model_Category_Root_EN',
            'memory_size': '_Memory_Size_Category_Root_EN',
            'storage_capacity': '_Storage_Capacity_Category_Root_EN',
            'storage_type': '_Storage_Type_Category_Root_EN',
            'screen_size': '_Screen_Size_Category_Root_EN',
            'screen_resolution': '_Screen_Resolution_Category_Root_EN',
            'operating_system': '_Operating_System_Category_Root_EN',
            'color': '_Color_Category_Root_EN',
            'price': '_Price_Category_Root_EN',
            'msrp': '_MSRP_Category_Root_EN',
            'quantity': '_Quantity_Category_Root_EN',
            'weight': '_Weight_Category_Root_EN',
            'dimensions': '_Dimensions_Category_Root_EN'
        }
        
        # Process each field
        for form_field, template_field in field_mapping.items():
            if form_field in form_data:
                value = form_data[form_field]
                
                # Validate field
                is_valid, error_message = self.validator.validate_field(
                    template_field, value, form_data
                )
                
                if not is_valid:
                    validation_errors[form_field] = error_message
                else:
                    processed_data[template_field] = self._transform_value(
                        template_field, value, form_data
                    )
        
        # Auto-generate missing required fields
        processed_data = self._auto_generate_fields(processed_data, form_data)
        
        return {
            'data': processed_data,
            'validation_errors': validation_errors,
            'is_valid': len(validation_errors) == 0
        }
    
    def _transform_value(self, field_code: str, value: Any, context: Dict) -> Any:
        """Transform value based on field requirements"""
        
        # Title transformation - ensure condition suffix
        if field_code == '_Title_BB_Category_Root_EN':
            title = str(value).strip()
            condition = context.get('product_condition', '')
            if condition and not title.endswith(f" - {condition}"):
                return f"{title} - {condition}"
            return title
        
        # SKU transformation - ensure uppercase
        if field_code == 'shop_sku':
            return str(value).upper().strip()
        
        # Numeric fields
        if field_code in ['_Price_Category_Root_EN', '_MSRP_Category_Root_EN']:
            try:
                return float(value) if value else None
            except (ValueError, TypeError):
                return None
        
        if field_code in ['_Quantity_Category_Root_EN', '_Memory_Size_Category_Root_EN', '_Storage_Capacity_Category_Root_EN']:
            try:
                return int(value) if value else None
            except (ValueError, TypeError):
                return None
        
        # Default: return as string
        return str(value).strip() if value else ""
    
    def _auto_generate_fields(self, processed_data: Dict, form_data: Dict) -> Dict:
        """Auto-generate missing required fields where possible"""
        
        # Auto-generate MPN if missing
        if '_Manufacturers_Part_Number_Category_Root_EN' not in processed_data:
            model_number = processed_data.get('_Model_Number_Category_Root_EN', '')
            if model_number:
                processed_data['_Manufacturers_Part_Number_Category_Root_EN'] = model_number
        
        # Auto-generate web hierarchy if missing but category code exists
        if '_Web_Hierarchy_Location_Category_Root_EN' not in processed_data:
            category_code = processed_data.get('BBYCat', '')
            if category_code:
                processed_data['_Web_Hierarchy_Location_Category_Root_EN'] = category_code
        
        # Auto-generate variant group if missing
        if '_Variant_Group_Category_Root_EN' not in processed_data:
            sku = processed_data.get('shop_sku', '')
            platform = processed_data.get('_Platform_Category_Root_EN', '')
            if sku and platform:
                # Extract base from SKU and add platform suffix
                sku_base = '-'.join(sku.split('-')[:2])  # Brand-Model
                platform_suffix = 'win' if 'PC' in platform else 'gaming' if 'Gaming' in platform else 'mac'
                processed_data['_Variant_Group_Category_Root_EN'] = f"{sku_base.lower()}-{platform_suffix}"
        
        return processed_data

class BestBuyTemplateGenerator:
    """Generate Best Buy Excel templates from processed data"""
    
    def __init__(self):
        self.processor = BestBuyDataProcessor()
        self.template_path = '/home/ubuntu/upload/AS-i7-Export.xlsx'
    
    def generate_template(self, form_data: Dict, output_path: str = None) -> Dict:
        """
        Generate Best Buy template from form data
        
        Args:
            form_data: Form data from frontend
            output_path: Path to save generated template
            
        Returns:
            Generation result with status and file path
        """
        try:
            # Process form data
            processed_result = self.processor.process_form_data(form_data)
            
            if not processed_result['is_valid']:
                return {
                    'success': False,
                    'errors': processed_result['validation_errors'],
                    'message': 'Validation errors found'
                }
            
            # Load template structure
            template_df = self._load_template_structure()
            
            # Populate template with processed data
            populated_df = self._populate_template(template_df, processed_result['data'])
            
            # Generate output path if not provided
            if not output_path:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                sku = processed_result['data'].get('shop_sku', 'listing')
                output_path = f"/home/ubuntu/bestbuy_listing_{sku}_{timestamp}.xlsx"
            
            # Save template
            self._save_template(populated_df, output_path)
            
            return {
                'success': True,
                'file_path': output_path,
                'message': 'Template generated successfully',
                'data_summary': self._generate_summary(processed_result['data'])
            }
            
        except Exception as e:
            logger.error(f"Error generating template: {e}")
            return {
                'success': False,
                'message': f'Error generating template: {str(e)}'
            }
    
    def _load_template_structure(self) -> pd.DataFrame:
        """Load the template structure from the reference file"""
        try:
            # Load the main data sheet
            df = pd.read_excel(self.template_path, sheet_name=0)
            
            # Create empty template with same structure
            empty_template = pd.DataFrame(columns=df.columns)
            
            return empty_template
            
        except Exception as e:
            logger.error(f"Error loading template structure: {e}")
            # Create minimal template structure
            return pd.DataFrame(columns=[
                'BBYCat', 'shop_sku', '_Title_BB_Category_Root_EN',
                '_Short_Description_BB_Category_Root_EN', '_Brand_Name_Category_Root_EN'
            ])
    
    def _populate_template(self, template_df: pd.DataFrame, data: Dict) -> pd.DataFrame:
        """Populate template with processed data"""
        
        # Create new row with data
        new_row = {}
        
        # Map data to template columns
        for column in template_df.columns:
            if column in data:
                new_row[column] = data[column]
            else:
                new_row[column] = ""  # Empty string for missing fields
        
        # Add the row to template
        populated_df = pd.concat([template_df, pd.DataFrame([new_row])], ignore_index=True)
        
        return populated_df
    
    def _save_template(self, df: pd.DataFrame, output_path: str):
        """Save populated template to Excel file"""
        try:
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Listing Data', index=False)
                
                # Add reference sheets if available
                try:
                    columns_df = pd.read_excel(self.template_path, sheet_name='Columns')
                    columns_df.to_excel(writer, sheet_name='Columns', index=False)
                except:
                    pass  # Reference sheet not available
            
            logger.info(f"Template saved to: {output_path}")
            
        except Exception as e:
            logger.error(f"Error saving template: {e}")
            raise
    
    def _generate_summary(self, data: Dict) -> Dict:
        """Generate summary of processed data"""
        return {
            'sku': data.get('shop_sku', 'N/A'),
            'title': data.get('_Title_BB_Category_Root_EN', 'N/A'),
            'brand': data.get('_Brand_Name_Category_Root_EN', 'N/A'),
            'category': data.get('BBYCat', 'N/A'),
            'condition': data.get('_Product_Condition_Category_Root_EN', 'N/A'),
            'fields_populated': len([v for v in data.values() if v])
        }

class BestBuyListingManager:
    """Main class for managing Best Buy listing operations"""
    
    def __init__(self):
        self.generator = BestBuyTemplateGenerator()
        self.validator = BestBuyFieldValidator()
    
    def create_listing(self, form_data: Dict) -> Dict:
        """
        Create a new Best Buy listing from form data
        
        Args:
            form_data: Complete form data from frontend
            
        Returns:
            Creation result with template file and validation status
        """
        logger.info(f"Creating listing for SKU: {form_data.get('shop_sku', 'Unknown')}")
        
        # Generate template
        result = self.generator.generate_template(form_data)
        
        if result['success']:
            logger.info(f"Listing created successfully: {result['file_path']}")
        else:
            logger.error(f"Listing creation failed: {result['message']}")
        
        return result
    
    def validate_listing_data(self, form_data: Dict) -> Dict:
        """
        Validate listing data without generating template
        
        Args:
            form_data: Form data to validate
            
        Returns:
            Validation result
        """
        processed_result = self.generator.processor.process_form_data(form_data)
        
        return {
            'is_valid': processed_result['is_valid'],
            'errors': processed_result['validation_errors'],
            'warnings': self._generate_warnings(processed_result['data'])
        }
    
    def _generate_warnings(self, data: Dict) -> List[str]:
        """Generate warnings for potential issues"""
        warnings = []
        
        # Check for missing recommended fields
        recommended_fields = [
            '_Platform_Category_Root_EN',
            '_Variant_Group_Category_Root_EN',
            '_Processor_Brand_Category_Root_EN',
            '_Memory_Size_Category_Root_EN',
            '_Storage_Capacity_Category_Root_EN'
        ]
        
        for field in recommended_fields:
            if field not in data or not data[field]:
                field_name = field.replace('_Category_Root_EN', '').replace('_', ' ').title()
                warnings.append(f"Recommended field missing: {field_name}")
        
        # Check for potential pricing issues
        price = data.get('_Price_Category_Root_EN')
        msrp = data.get('_MSRP_Category_Root_EN')
        
        if price and msrp and float(price) > float(msrp):
            warnings.append("Price is higher than MSRP")
        
        return warnings

# Example usage and testing
if __name__ == "__main__":
    # Test data
    test_form_data = {
        'shop_sku': 'AS-I7-16-512',
        'title': 'ASUS Vivobook Laptop - Refurbished (Excellent)',
        'short_description': 'High-performance laptop with Intel i7 processor, perfect for business and productivity tasks.',
        'long_description': '• Intel i7 processor for superior performance\n• 16GB RAM for smooth multitasking\n• 512GB SSD for fast boot times\n• 15.6-inch Full HD display\n• Windows 11 operating system',
        'brand_name': 'ASUS',
        'model_number': 'Vivobook',
        'mpn': 'Vivobook',
        'product_condition': 'Refurbished (Excellent)',
        'category_code': 'BB_36711',
        'web_hierarchy': 'BB_36711',
        'platform': 'PC Laptop',
        'variant_group': 'as-i7-win',
        'processor_brand': 'Intel',
        'processor_model': 'Core i7-12700H',
        'memory_size': '16',
        'storage_capacity': '512',
        'storage_type': 'SSD',
        'screen_size': '15.6',
        'screen_resolution': '1920 x 1080',
        'operating_system': 'Windows 11',
        'color': 'Silver',
        'price': '999.99',
        'msrp': '1299.99',
        'quantity': '10',
        'weight': '4.5',
        'dimensions': '14.1 x 9.2 x 0.7 inches'
    }
    
    # Test the system
    manager = BestBuyListingManager()
    
    print("Testing Best Buy Listing System...")
    print("=" * 50)
    
    # Test validation
    validation_result = manager.validate_listing_data(test_form_data)
    print(f"Validation Result: {validation_result}")
    
    # Test template generation
    if validation_result['is_valid']:
        creation_result = manager.create_listing(test_form_data)
        print(f"Creation Result: {creation_result}")
    
    print("Testing completed!")

