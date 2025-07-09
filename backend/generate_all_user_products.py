#!/usr/bin/env python3
"""
Generate all user products with working templates
"""

import pandas as pd
from datetime import datetime
import os

def create_field_mapping():
    """Create mapping from our data fields to template columns"""
    return {
        'shop_sku': 'Shop sku',
        '_Title_BB_Category_Root_EN': 'Title BB (EN)',
        '_Short_Description_BB_Category_Root_EN': 'Short Description BB (EN)',
        '_Long_Description_Category_Root_EN': 'Long Description BB (EN)',
        '_Brand_Name_Category_Root_EN': 'Brand Name',
        '_Model_Number_Category_Root_EN': 'Model Number',
        '_Manufacturers_Part_Number_Category_Root_EN': "Manufacturer's Part Number",
        '_Product_Condition_Category_Root_EN': 'Product Condition',
        'BBYCat': 'Category Code',
        '_Web_Hierarchy_Location_Category_Root_EN': 'Web Hierarchy Location',
        '_Platform_Category_Root_EN': 'Platform',
        '_Variant_Group_Category_Root_EN': 'Variant Group',
        '_Processor_Brand_Category_Root_EN': 'Processor Brand',
        '_Processor_Model_Category_Root_EN': 'Processor Model',
        '_Memory_Size_Category_Root_EN': 'Memory Size',
        '_Storage_Capacity_Category_Root_EN': 'Storage Capacity',
        '_Storage_Type_Category_Root_EN': 'Storage Type',
        '_Screen_Size_Category_Root_EN': 'Screen Size',
        '_Screen_Resolution_Category_Root_EN': 'Screen Resolution',
        '_Operating_System_Category_Root_EN': 'Operating System',
        '_Color_Category_Root_EN': 'Color',
        '_Price_Category_Root_EN': 'Price',
        '_MSRP_Category_Root_EN': 'MSRP',
        '_Quantity_Category_Root_EN': 'Quantity',
        '_Weight_Category_Root_EN': 'Weight',
        '_Dimensions_Category_Root_EN': 'Dimensions'
    }

def create_all_products():
    """Create all user products"""
    products = []
    
    # 2x Acer Spin SP5-143-52N-5621
    for i in range(2):
        products.append({
            'shop_sku': f'AC-SP5-8-512-{i+1}',
            '_Title_BB_Category_Root_EN': 'Acer Spin 5 SP5-143-52N-5621 Convertible Laptop - Refurbished (Excellent)',
            '_Short_Description_BB_Category_Root_EN': 'Versatile 2-in-1 convertible laptop with touchscreen display, perfect for productivity and creativity tasks.',
            '_Long_Description_Category_Root_EN': '• Intel processor for reliable performance\n• 8GB RAM for smooth multitasking\n• 512GB SSD for fast boot times and storage\n• x360 touchscreen display for versatile use\n• Convertible design for laptop and tablet modes\n• Windows operating system',
            '_Brand_Name_Category_Root_EN': 'Acer',
            '_Model_Number_Category_Root_EN': 'Spin 5',
            '_Manufacturers_Part_Number_Category_Root_EN': 'SP5-143-52N-5621',
            '_Product_Condition_Category_Root_EN': 'Refurbished (Excellent)',
            'BBYCat': 'BB_36711',
            '_Web_Hierarchy_Location_Category_Root_EN': 'BB_36711',
            '_Platform_Category_Root_EN': 'PC Laptop',
            '_Variant_Group_Category_Root_EN': 'acer-spin5-win',
            '_Processor_Brand_Category_Root_EN': 'Intel',
            '_Processor_Model_Category_Root_EN': 'Core i5',
            '_Memory_Size_Category_Root_EN': '8',
            '_Storage_Capacity_Category_Root_EN': '512',
            '_Storage_Type_Category_Root_EN': 'SSD',
            '_Screen_Size_Category_Root_EN': '14',
            '_Screen_Resolution_Category_Root_EN': '1920 x 1080',
            '_Operating_System_Category_Root_EN': 'Windows 11',
            '_Color_Category_Root_EN': 'Silver',
            '_Price_Category_Root_EN': '649.99',
            '_MSRP_Category_Root_EN': '899.99',
            '_Quantity_Category_Root_EN': '1',
            '_Weight_Category_Root_EN': '3.2',
            '_Dimensions_Category_Root_EN': '12.8 x 8.9 x 0.6 inches'
        })
    
    # HP 15dy2228ca i7 - Brand New & Open Box
    for condition, price, suffix in [('Brand New', '1299.99', 'BN'), ('Open Box', '1199.99', 'OB')]:
        products.append({
            'shop_sku': f'HP-15DY-32-1000-{suffix}',
            '_Title_BB_Category_Root_EN': f'HP 15dy2228ca Laptop Intel i7 Non-Touch - {condition}',
            '_Short_Description_BB_Category_Root_EN': 'High-performance HP laptop with Intel i7 processor, ideal for professional and personal computing needs.',
            '_Long_Description_Category_Root_EN': '• Intel i7 processor for superior performance\n• 32GB RAM for exceptional multitasking\n• 1TB SSD for massive storage and fast access\n• 15.6-inch non-touch display\n• Professional design for business use\n• Windows 11 operating system',
            '_Brand_Name_Category_Root_EN': 'HP',
            '_Model_Number_Category_Root_EN': '15dy2228ca',
            '_Manufacturers_Part_Number_Category_Root_EN': '15dy2228ca',
            '_Product_Condition_Category_Root_EN': condition,
            'BBYCat': 'BB_36711',
            '_Web_Hierarchy_Location_Category_Root_EN': 'BB_36711',
            '_Platform_Category_Root_EN': 'PC Laptop',
            '_Variant_Group_Category_Root_EN': 'hp-15dy-win',
            '_Processor_Brand_Category_Root_EN': 'Intel',
            '_Processor_Model_Category_Root_EN': 'Core i7',
            '_Memory_Size_Category_Root_EN': '32',
            '_Storage_Capacity_Category_Root_EN': '1000',
            '_Storage_Type_Category_Root_EN': 'SSD',
            '_Screen_Size_Category_Root_EN': '15.6',
            '_Screen_Resolution_Category_Root_EN': '1920 x 1080',
            '_Operating_System_Category_Root_EN': 'Windows 11',
            '_Color_Category_Root_EN': 'Silver',
            '_Price_Category_Root_EN': price,
            '_MSRP_Category_Root_EN': '1599.99',
            '_Quantity_Category_Root_EN': '1',
            '_Weight_Category_Root_EN': '4.1',
            '_Dimensions_Category_Root_EN': '14.1 x 9.5 x 0.7 inches'
        })
    
    # Dell products
    dell_products = [
        ('DE-3390-32-2000', 'Dell Latitude 3390 Touchscreen Laptop', 'Latitude 3390', 'Latitude 3390', '32', '2000', '13.3', '899.99', '1299.99', '3.1', '12.4 x 8.3 x 0.7 inches'),
        ('DE-3520-32-2000', 'Dell Inspiron 3520 Non-Touch Laptop', 'Inspiron 3520', 'Inspiron 3520', '32', '2000', '15.6', '799.99', '1199.99', '4.2', '14.3 x 9.7 x 0.8 inches'),
        ('DE-7390-32-1000', 'Dell Latitude 7390 Business Laptop', 'Latitude 7390', 'Latitude 7390', '32', '1000', '13.3', '999.99', '1499.99', '2.9', '12.1 x 8.2 x 0.6 inches'),
        ('DE-7390-16-512', 'Dell Latitude 7390 Business Laptop', 'Latitude 7390', 'Latitude 7390', '16', '512', '13.3', '749.99', '1299.99', '2.9', '12.1 x 8.2 x 0.6 inches')
    ]
    
    for sku, title, model, mpn, ram, storage, screen, price, msrp, weight, dimensions in dell_products:
        products.append({
            'shop_sku': sku,
            '_Title_BB_Category_Root_EN': f'{title} - Refurbished (Excellent)',
            '_Short_Description_BB_Category_Root_EN': 'Premium Dell business laptop with professional features and high-end specifications.',
            '_Long_Description_Category_Root_EN': f'• Intel processor for professional performance\n• {ram}GB RAM for advanced multitasking\n• {storage}GB SSD for fast storage and boot times\n• {screen}-inch professional display\n• Business-grade security features\n• Windows 11 operating system',
            '_Brand_Name_Category_Root_EN': 'Dell',
            '_Model_Number_Category_Root_EN': model,
            '_Manufacturers_Part_Number_Category_Root_EN': mpn,
            '_Product_Condition_Category_Root_EN': 'Refurbished (Excellent)',
            'BBYCat': 'BB_36711',
            '_Web_Hierarchy_Location_Category_Root_EN': 'BB_36711',
            '_Platform_Category_Root_EN': 'PC Laptop',
            '_Variant_Group_Category_Root_EN': f'dell-{model.lower().replace(" ", "")}-win',
            '_Processor_Brand_Category_Root_EN': 'Intel',
            '_Processor_Model_Category_Root_EN': 'Core i7' if '7390' in sku else 'Core i5',
            '_Memory_Size_Category_Root_EN': ram,
            '_Storage_Capacity_Category_Root_EN': storage,
            '_Storage_Type_Category_Root_EN': 'SSD',
            '_Screen_Size_Category_Root_EN': screen,
            '_Screen_Resolution_Category_Root_EN': '1920 x 1080',
            '_Operating_System_Category_Root_EN': 'Windows 11',
            '_Color_Category_Root_EN': 'Black',
            '_Price_Category_Root_EN': price,
            '_MSRP_Category_Root_EN': msrp,
            '_Quantity_Category_Root_EN': '1',
            '_Weight_Category_Root_EN': weight,
            '_Dimensions_Category_Root_EN': dimensions
        })
    
    # Lenovo ThinkPad E590 products
    thinkpad_products = [
        ('LE-E590-32-512', 'Lenovo ThinkPad E590 i5 Business Laptop', 'ThinkPad E590', 'ThinkPad E590', 'Core i5', '32', '512', '699.99', '999.99'),
        ('LE-E590-32-1000', 'Lenovo ThinkPad E590 i5 Business Laptop', 'ThinkPad E590', 'ThinkPad E590', 'Core i5', '32', '1000', '799.99', '1199.99'),
        ('LE-E590-32-2000', 'Lenovo ThinkPad E590 i5 Business Laptop', 'ThinkPad E590', 'ThinkPad E590', 'Core i5', '32', '2000', '899.99', '1399.99'),
        ('LE-E590-64-2000', 'Lenovo ThinkPad E590 20nb001jus Business Laptop', 'ThinkPad E590', '20nb001jus', 'Core i7', '64', '2000', '1299.99', '1899.99'),
        ('LE-E590-32-1000-2', 'Lenovo ThinkPad E590 20nb001jus Business Laptop', 'ThinkPad E590', '20nb001jus', 'Core i7', '32', '1000', '999.99', '1499.99')
    ]
    
    for sku, title, model, mpn, processor, ram, storage, price, msrp in thinkpad_products:
        products.append({
            'shop_sku': sku,
            '_Title_BB_Category_Root_EN': f'{title} - Refurbished (Excellent)',
            '_Short_Description_BB_Category_Root_EN': 'Reliable ThinkPad business laptop with legendary keyboard and build quality.',
            '_Long_Description_Category_Root_EN': f'• Intel {processor} processor for professional performance\n• {ram}GB RAM for excellent multitasking\n• {storage}GB SSD for fast storage and responsiveness\n• 15.6-inch business display\n• ThinkPad legendary keyboard\n• Windows 11 operating system',
            '_Brand_Name_Category_Root_EN': 'Lenovo',
            '_Model_Number_Category_Root_EN': model,
            '_Manufacturers_Part_Number_Category_Root_EN': mpn,
            '_Product_Condition_Category_Root_EN': 'Refurbished (Excellent)',
            'BBYCat': 'BB_36711',
            '_Web_Hierarchy_Location_Category_Root_EN': 'BB_36711',
            '_Platform_Category_Root_EN': 'PC Laptop',
            '_Variant_Group_Category_Root_EN': 'lenovo-e590-win',
            '_Processor_Brand_Category_Root_EN': 'Intel',
            '_Processor_Model_Category_Root_EN': processor,
            '_Memory_Size_Category_Root_EN': ram,
            '_Storage_Capacity_Category_Root_EN': storage,
            '_Storage_Type_Category_Root_EN': 'SSD',
            '_Screen_Size_Category_Root_EN': '15.6',
            '_Screen_Resolution_Category_Root_EN': '1920 x 1080',
            '_Operating_System_Category_Root_EN': 'Windows 11',
            '_Color_Category_Root_EN': 'Black',
            '_Price_Category_Root_EN': price,
            '_MSRP_Category_Root_EN': msrp,
            '_Quantity_Category_Root_EN': '1',
            '_Weight_Category_Root_EN': '4.7',
            '_Dimensions_Category_Root_EN': '14.2 x 9.8 x 0.9 inches'
        })
    
    # HP Pavilion 15
    products.append({
        'shop_sku': 'HP-PAV15-32-1000',
        '_Title_BB_Category_Root_EN': 'HP Pavilion 15 ER-0008ca Non-Touch Laptop - Refurbished (Excellent)',
        '_Short_Description_BB_Category_Root_EN': 'Stylish HP Pavilion laptop with powerful specifications, perfect for multimedia and productivity.',
        '_Long_Description_Category_Root_EN': '• Intel processor for reliable performance\n• 32GB RAM for smooth multitasking\n• 1TB SSD for ample storage and fast access\n• 15.6-inch non-touch display\n• Modern design with premium features\n• Windows 11 operating system',
        '_Brand_Name_Category_Root_EN': 'HP',
        '_Model_Number_Category_Root_EN': 'Pavilion 15',
        '_Manufacturers_Part_Number_Category_Root_EN': 'ER-0008ca',
        '_Product_Condition_Category_Root_EN': 'Refurbished (Excellent)',
        'BBYCat': 'BB_36711',
        '_Web_Hierarchy_Location_Category_Root_EN': 'BB_36711',
        '_Platform_Category_Root_EN': 'PC Laptop',
        '_Variant_Group_Category_Root_EN': 'hp-pavilion15-win',
        '_Processor_Brand_Category_Root_EN': 'Intel',
        '_Processor_Model_Category_Root_EN': 'Core i5',
        '_Memory_Size_Category_Root_EN': '32',
        '_Storage_Capacity_Category_Root_EN': '1000',
        '_Storage_Type_Category_Root_EN': 'SSD',
        '_Screen_Size_Category_Root_EN': '15.6',
        '_Screen_Resolution_Category_Root_EN': '1920 x 1080',
        '_Operating_System_Category_Root_EN': 'Windows 11',
        '_Color_Category_Root_EN': 'Silver',
        '_Price_Category_Root_EN': '849.99',
        '_MSRP_Category_Root_EN': '1199.99',
        '_Quantity_Category_Root_EN': '1',
        '_Weight_Category_Root_EN': '4.0',
        '_Dimensions_Category_Root_EN': '14.1 x 9.5 x 0.7 inches'
    })
    
    return products

def create_working_template(product_data, output_filename):
    """Create a working template with proper field mapping"""
    
    # Load the original template structure
    original_df = pd.read_excel('/home/ubuntu/upload/AS-i7-Export.xlsx')
    
    # Create empty template with same columns
    template_df = pd.DataFrame(columns=original_df.columns)
    
    # Create field mapping
    field_mapping = create_field_mapping()
    
    # Create new row
    new_row = {}
    
    # Initialize all columns with empty strings
    for col in template_df.columns:
        new_row[col] = ""
    
    # Map our data to the correct columns
    mapped_count = 0
    for our_field, template_column in field_mapping.items():
        if our_field in product_data and template_column in template_df.columns:
            value = product_data[our_field]
            if value is not None and str(value).strip():
                new_row[template_column] = value
                mapped_count += 1
    
    # Add the row to template
    populated_df = pd.concat([template_df, pd.DataFrame([new_row])], ignore_index=True)
    
    # Save the template
    with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
        populated_df.to_excel(writer, sheet_name='Data', index=False)
        
        # Add reference sheets
        try:
            ref_df = pd.read_excel('/home/ubuntu/upload/AS-i7-Export.xlsx', sheet_name='ReferenceData')
            ref_df.to_excel(writer, sheet_name='ReferenceData', index=False)
        except:
            pass
        
        try:
            col_df = pd.read_excel('/home/ubuntu/upload/AS-i7-Export.xlsx', sheet_name='Columns')
            col_df.to_excel(writer, sheet_name='Columns', index=False)
        except:
            pass
    
    return mapped_count, len(template_df.columns)

def main():
    """Generate all working templates"""
    print("🚀 GENERATING ALL USER PRODUCT TEMPLATES")
    print("=" * 60)
    
    products = create_all_products()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    successful_templates = []
    failed_templates = []
    
    for i, product in enumerate(products, 1):
        sku = product['shop_sku']
        output_filename = f"/home/ubuntu/final_bestbuy_listing_{sku}_{timestamp}.xlsx"
        
        print(f"Creating template {i:2d}/{len(products)}: {sku}")
        
        try:
            mapped_count, total_columns = create_working_template(product, output_filename)
            
            # Verify the template
            verify_df = pd.read_excel(output_filename, sheet_name='Data')
            
            if len(verify_df) > 0:
                row = verify_df.iloc[0]
                title = row.get('Title BB (EN)', 'N/A')
                brand = row.get('Brand Name', 'N/A')
                
                print(f"    ✅ Success: {mapped_count} fields mapped")
                print(f"    📋 Title: {title[:60]}{'...' if len(title) > 60 else ''}")
                
                successful_templates.append({
                    'sku': sku,
                    'filename': output_filename,
                    'title': title,
                    'brand': brand,
                    'mapped_fields': mapped_count
                })
            else:
                print(f"    ❌ Template is empty")
                failed_templates.append(sku)
                
        except Exception as e:
            print(f"    ❌ Error: {e}")
            failed_templates.append(sku)
    
    # Create ZIP package
    print(f"\n📦 Creating ZIP package...")
    zip_filename = f"/home/ubuntu/final_bestbuy_templates_{timestamp}.zip"
    
    if successful_templates:
        import subprocess
        file_list = [template['filename'] for template in successful_templates]
        cmd = ['zip', zip_filename] + file_list
        subprocess.run(cmd, cwd='/home/ubuntu')
        print(f"    ✅ ZIP created: {os.path.basename(zip_filename)}")
    
    # Create summary
    print("\n" + "=" * 60)
    print(f"🎉 BATCH PROCESSING COMPLETE")
    print(f"Total products: {len(products)}")
    print(f"Successful: {len(successful_templates)}")
    print(f"Failed: {len(failed_templates)}")
    print(f"Success rate: {(len(successful_templates)/len(products)*100):.1f}%")
    
    if successful_templates:
        print(f"\n✅ SUCCESSFUL TEMPLATES:")
        for template in successful_templates:
            filename = os.path.basename(template['filename'])
            print(f"  • {template['sku']}: {template['brand']} - {template['mapped_fields']} fields")
    
    if failed_templates:
        print(f"\n❌ FAILED TEMPLATES:")
        for sku in failed_templates:
            print(f"  • {sku}")
    
    return successful_templates, zip_filename

if __name__ == "__main__":
    templates, zip_file = main()

