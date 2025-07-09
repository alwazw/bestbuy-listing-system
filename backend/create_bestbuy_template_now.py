#!/usr/bin/env python3
"""
URGENT: Best Buy Template Generator with Live Monitoring
Creates professional listings for all 14 products immediately
"""

import pandas as pd
import json
import time
import sys
from datetime import datetime

def log_progress(message):
    """Log progress with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")
    sys.stdout.flush()

def create_all_products():
    """Create all 14 products immediately"""
    log_progress("🚀 STARTING BEST BUY TEMPLATE GENERATION")
    
    products = []
    
    # Product 1: Acer Spin 5 SP513-52N-5621 #1
    log_progress("Creating Product 1: Acer Spin 5 #1")
    products.append({
        "Shop sku": "AC-SP5-8-512-1",
        "Title BB (EN)": "Acer Spin 5 SP513-52N-5621 13.3\" Full HD Touchscreen 2-in-1 Convertible Laptop - Intel Core i5-8250U, 8GB DDR4, 512GB SSD, Windows 10 Home",
        "Brand Name": "Acer",
        "Model Number": "SP513-52N-5621",
        "Short Description (EN)": "Versatile 2-in-1 convertible laptop with 360-degree hinge, Full HD touchscreen, and powerful Intel Core i5 processor for productivity and entertainment.",
        "Long Description (EN)": "Experience ultimate versatility with the Acer Spin 5 2-in-1 convertible laptop. Featuring a premium 360-degree hinge design, this laptop seamlessly transforms between laptop, tablet, tent, and display modes to adapt to your workflow. The vibrant 13.3-inch Full HD IPS touchscreen delivers crisp visuals with wide viewing angles, while the Intel Core i5-8250U quad-core processor ensures smooth performance for multitasking, productivity applications, and light gaming. With 8GB of fast DDR4 memory and a spacious 512GB SSD, you'll enjoy quick boot times and ample storage for your files and applications. The backlit keyboard enables comfortable typing in any lighting condition, while the fingerprint reader provides secure, one-touch login. Built for professionals and students alike, this laptop combines style, performance, and flexibility in a sleek, portable design.",
        "Condition": "Brand New",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i5",
        "Processor Model": "i5-8250U",
        "Processor Speed": "1.6 GHz",
        "Memory (RAM)": "8 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "512 GB",
        "Storage Type": "SSD",
        "Screen Size": "13.3 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "Yes",
        "Graphics": "Intel UHD Graphics 620",
        "Operating System": "Windows 10 Home",
        "Weight": "3.3 lbs",
        "Color": "Steel Gray",
        "Image URL 1": "https://images.acer.com/is/image/acer/acer-spin-5-sp513-52n-steel-gray-01"
    })
    
    # Product 2: Acer Spin 5 SP513-52N-5621 #2
    log_progress("Creating Product 2: Acer Spin 5 #2")
    products.append({
        "Shop sku": "AC-SP5-8-512-2",
        "Title BB (EN)": "Acer Spin 5 SP513-52N-5621 13.3\" Full HD Touchscreen 2-in-1 Convertible Laptop - Intel Core i5-8250U, 8GB DDR4, 512GB SSD, Windows 10 Home",
        "Brand Name": "Acer",
        "Model Number": "SP513-52N-5621",
        "Short Description (EN)": "Versatile 2-in-1 convertible laptop with 360-degree hinge, Full HD touchscreen, and powerful Intel Core i5 processor for productivity and entertainment.",
        "Long Description (EN)": "Experience ultimate versatility with the Acer Spin 5 2-in-1 convertible laptop. Featuring a premium 360-degree hinge design, this laptop seamlessly transforms between laptop, tablet, tent, and display modes to adapt to your workflow. The vibrant 13.3-inch Full HD IPS touchscreen delivers crisp visuals with wide viewing angles, while the Intel Core i5-8250U quad-core processor ensures smooth performance for multitasking, productivity applications, and light gaming. With 8GB of fast DDR4 memory and a spacious 512GB SSD, you'll enjoy quick boot times and ample storage for your files and applications. The backlit keyboard enables comfortable typing in any lighting condition, while the fingerprint reader provides secure, one-touch login. Built for professionals and students alike, this laptop combines style, performance, and flexibility in a sleek, portable design.",
        "Condition": "Brand New",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i5",
        "Processor Model": "i5-8250U",
        "Processor Speed": "1.6 GHz",
        "Memory (RAM)": "8 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "512 GB",
        "Storage Type": "SSD",
        "Screen Size": "13.3 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "Yes",
        "Graphics": "Intel UHD Graphics 620",
        "Operating System": "Windows 10 Home",
        "Weight": "3.3 lbs",
        "Color": "Steel Gray",
        "Image URL 1": "https://images.acer.com/is/image/acer/acer-spin-5-sp513-52n-steel-gray-01"
    })
    
    # Product 3: HP 15dy2228ca i7 - Brand New
    log_progress("Creating Product 3: HP 15dy2228ca - Brand New")
    products.append({
        "Shop sku": "HP-15DY-32-1000-BN",
        "Title BB (EN)": "HP 15-dy2228ca 15.6\" Full HD Laptop - Intel Core i7-1165G7, 32GB DDR4, 1TB SSD, Intel Iris Xe Graphics, Windows 11 Home - Brand New",
        "Brand Name": "HP",
        "Model Number": "15-dy2228ca",
        "Short Description (EN)": "High-performance 15.6-inch laptop with 11th Gen Intel Core i7 processor, massive 32GB RAM, and lightning-fast 1TB SSD for professional productivity and multitasking.",
        "Long Description (EN)": "Elevate your productivity with the HP 15-dy2228ca, a powerhouse laptop engineered for demanding professional workloads and intensive multitasking. Powered by the latest 11th Generation Intel Core i7-1165G7 processor with Intel Iris Xe graphics, this laptop delivers exceptional performance for content creation, data analysis, and business applications. The generous 32GB of DDR4 memory ensures seamless multitasking across multiple applications, while the spacious 1TB PCIe NVMe SSD provides lightning-fast boot times and ample storage for large files, projects, and media libraries. The crisp 15.6-inch Full HD display offers excellent clarity for extended work sessions, complemented by a comfortable full-size keyboard with numeric keypad for efficient data entry. Advanced connectivity options including USB-C, multiple USB-A ports, and HDMI ensure compatibility with all your peripherals and external displays. Perfect for business professionals, content creators, and power users who demand reliable performance and expandability.",
        "Condition": "Brand New",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i7",
        "Processor Model": "i7-1165G7",
        "Processor Speed": "2.8 GHz",
        "Memory (RAM)": "32 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "1 TB",
        "Storage Type": "SSD",
        "Screen Size": "15.6 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel Iris Xe Graphics",
        "Operating System": "Windows 11 Home",
        "Weight": "3.75 lbs",
        "Color": "Natural Silver",
        "Image URL 1": "https://ssl-product-images.www8-hp.com/digmedialib/prodimg/lowres/c07791334.png"
    })
    
    # Product 4: HP 15dy2228ca i7 - Open Box
    log_progress("Creating Product 4: HP 15dy2228ca - Open Box")
    products.append({
        "Shop sku": "HP-15DY-32-1000-OB",
        "Title BB (EN)": "HP 15-dy2228ca 15.6\" Full HD Laptop - Intel Core i7-1165G7, 32GB DDR4, 1TB SSD, Intel Iris Xe Graphics, Windows 11 Home - Open Box",
        "Brand Name": "HP",
        "Model Number": "15-dy2228ca",
        "Short Description (EN)": "High-performance 15.6-inch laptop with 11th Gen Intel Core i7 processor, massive 32GB RAM, and lightning-fast 1TB SSD for professional productivity and multitasking.",
        "Long Description (EN)": "Elevate your productivity with the HP 15-dy2228ca, a powerhouse laptop engineered for demanding professional workloads and intensive multitasking. Powered by the latest 11th Generation Intel Core i7-1165G7 processor with Intel Iris Xe graphics, this laptop delivers exceptional performance for content creation, data analysis, and business applications. The generous 32GB of DDR4 memory ensures seamless multitasking across multiple applications, while the spacious 1TB PCIe NVMe SSD provides lightning-fast boot times and ample storage for large files, projects, and media libraries. The crisp 15.6-inch Full HD display offers excellent clarity for extended work sessions, complemented by a comfortable full-size keyboard with numeric keypad for efficient data entry. Advanced connectivity options including USB-C, multiple USB-A ports, and HDMI ensure compatibility with all your peripherals and external displays. Perfect for business professionals, content creators, and power users who demand reliable performance and expandability. Open Box condition - item has been opened but is in excellent working condition with all original accessories.",
        "Condition": "Open Box",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i7",
        "Processor Model": "i7-1165G7",
        "Processor Speed": "2.8 GHz",
        "Memory (RAM)": "32 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "1 TB",
        "Storage Type": "SSD",
        "Screen Size": "15.6 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel Iris Xe Graphics",
        "Operating System": "Windows 11 Home",
        "Weight": "3.75 lbs",
        "Color": "Natural Silver",
        "Image URL 1": "https://ssl-product-images.www8-hp.com/digmedialib/prodimg/lowres/c07791334.png"
    })
    
    # Product 5: Dell Latitude 3390
    log_progress("Creating Product 5: Dell Latitude 3390")
    products.append({
        "Shop sku": "DL-3390-32-2000",
        "Title BB (EN)": "Dell Latitude 3390 2-in-1 13.3\" Full HD Touchscreen Business Laptop - Intel Core i5-8250U, 32GB DDR4, 2TB SSD, Windows 10 Pro",
        "Brand Name": "Dell",
        "Model Number": "Latitude 3390",
        "Short Description (EN)": "Professional-grade 2-in-1 business laptop with 360-degree hinge, Full HD touchscreen, and enterprise-level security features for demanding business environments.",
        "Long Description (EN)": "The Dell Latitude 3390 2-in-1 represents the pinnacle of business mobility, combining enterprise-grade security with versatile convertible design. This premium business laptop features a robust 360-degree hinge that transforms seamlessly between laptop, tablet, tent, and presentation modes, making it ideal for dynamic work environments. The 13.3-inch Full HD IPS touchscreen with anti-glare coating ensures excellent visibility in any lighting condition, while the Intel Core i5-8250U quad-core processor delivers reliable performance for business applications, video conferencing, and productivity tasks. Equipped with an impressive 32GB of DDR4 memory and a massive 2TB SSD, this configuration handles the most demanding professional workloads with ease, from large datasets to complex presentations. Enterprise-level security features include TPM 2.0, fingerprint reader, and IR camera for Windows Hello facial recognition. The durable construction meets MIL-STD-810G testing standards, ensuring reliability in challenging environments. Perfect for executives, consultants, and mobile professionals who require uncompromising performance and security.",
        "Condition": "Brand New",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i5",
        "Processor Model": "i5-8250U",
        "Processor Speed": "1.6 GHz",
        "Memory (RAM)": "32 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "2 TB",
        "Storage Type": "SSD",
        "Screen Size": "13.3 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "Yes",
        "Graphics": "Intel UHD Graphics 620",
        "Operating System": "Windows 10 Pro",
        "Weight": "3.17 lbs",
        "Color": "Black",
        "Image URL 1": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/latitude-notebooks/latitude-13-3390-2-in-1/media-gallery/latitude-3390-2-in-1-laptop-black-gallery-1.psd"
    })
    
    # Product 6: Dell Inspiron 3520 - Refurbished Excellent
    log_progress("Creating Product 6: Dell Inspiron 3520")
    products.append({
        "Shop sku": "DL-3520-32-2000-RE",
        "Title BB (EN)": "Dell Inspiron 3520 15.6\" Full HD Laptop - Intel Core i5-1235U, 32GB DDR4, 2TB SSD, Intel Iris Xe Graphics, Windows 11 Home - Refurbished (Excellent)",
        "Brand Name": "Dell",
        "Model Number": "Inspiron 3520",
        "Short Description (EN)": "Reliable 15.6-inch laptop with 12th Gen Intel Core i5 processor, upgraded 32GB RAM, and massive 2TB SSD storage for everyday computing and productivity tasks.",
        "Long Description (EN)": "The Dell Inspiron 3520 delivers dependable performance for everyday computing needs with modern 12th Generation Intel technology. Powered by the efficient Intel Core i5-1235U processor with Intel Iris Xe graphics, this laptop handles multitasking, web browsing, office applications, and light content creation with ease. The generous 32GB of DDR4 memory ensures smooth operation even with multiple applications running simultaneously, while the spacious 2TB SSD provides ample storage for documents, media files, and software installations with fast access times. The 15.6-inch Full HD display offers clear, vibrant visuals for work and entertainment, complemented by a comfortable keyboard for extended typing sessions. Modern connectivity options including USB-C, USB-A ports, HDMI, and Wi-Fi 6 ensure compatibility with current and future devices. This refurbished unit has been professionally tested and restored to excellent working condition, offering exceptional value for students, professionals, and home users who need reliable performance without compromise.",
        "Condition": "Refurbished (Excellent)",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i5",
        "Processor Model": "i5-1235U",
        "Processor Speed": "1.3 GHz",
        "Memory (RAM)": "32 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "2 TB",
        "Storage Type": "SSD",
        "Screen Size": "15.6 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel Iris Xe Graphics",
        "Operating System": "Windows 11 Home",
        "Weight": "3.82 lbs",
        "Color": "Carbon Black",
        "Image URL 1": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/inspiron-notebooks/inspiron-15-3520/media-gallery/inspiron-3520-laptop-carbon-black-gallery-1.psd"
    })
    
    # Product 7: Dell Latitude 7390 - 32GB RAM, 1TB SSD - Refurbished Excellent
    log_progress("Creating Product 7: Dell Latitude 7390 - 32GB/1TB")
    products.append({
        "Shop sku": "DL-7390-32-1000-RE",
        "Title BB (EN)": "Dell Latitude 7390 13.3\" Full HD Business Laptop - Intel Core i7-8650U, 32GB DDR4, 1TB SSD, Windows 10 Pro - Refurbished (Excellent)",
        "Brand Name": "Dell",
        "Model Number": "Latitude 7390",
        "Short Description (EN)": "Premium business ultrabook with 8th Gen Intel Core i7 processor, maximum 32GB RAM, and enterprise-grade security features for professional mobility.",
        "Long Description (EN)": "The Dell Latitude 7390 represents the ultimate in business mobility, combining premium performance with enterprise-grade security in an ultra-portable design. This professional ultrabook features the powerful Intel Core i7-8650U quad-core processor, delivering exceptional performance for demanding business applications, data analysis, and multitasking scenarios. With a maximum 32GB of DDR4 memory and a fast 1TB SSD, this configuration handles the most intensive professional workloads while providing ample storage for large files and applications. The 13.3-inch Full HD display with anti-glare coating ensures excellent visibility in any environment, while the premium keyboard and precision touchpad enhance productivity during long work sessions. Advanced security features include TPM 2.0, fingerprint reader, smart card reader, and optional IR camera for Windows Hello authentication. The durable carbon fiber construction meets MIL-STD-810G testing standards for reliability in challenging environments. This refurbished unit has been professionally restored to excellent condition, making it perfect for executives, consultants, and mobile professionals who demand uncompromising performance and security.",
        "Condition": "Refurbished (Excellent)",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i7",
        "Processor Model": "i7-8650U",
        "Processor Speed": "1.9 GHz",
        "Memory (RAM)": "32 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "1 TB",
        "Storage Type": "SSD",
        "Screen Size": "13.3 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel UHD Graphics 620",
        "Operating System": "Windows 10 Pro",
        "Weight": "2.87 lbs",
        "Color": "Black",
        "Image URL 1": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/latitude-notebooks/latitude-13-7390/media-gallery/latitude-7390-laptop-black-gallery-1.psd"
    })
    
    # Product 8: Dell Latitude 7390 - 16GB RAM, 512GB SSD - Refurbished Excellent
    log_progress("Creating Product 8: Dell Latitude 7390 - 16GB/512GB")
    products.append({
        "Shop sku": "DL-7390-16-512-RE",
        "Title BB (EN)": "Dell Latitude 7390 13.3\" Full HD Business Laptop - Intel Core i7-8650U, 16GB DDR4, 512GB SSD, Windows 10 Pro - Refurbished (Excellent)",
        "Brand Name": "Dell",
        "Model Number": "Latitude 7390",
        "Short Description (EN)": "Premium business ultrabook with 8th Gen Intel Core i7 processor, 16GB RAM, and enterprise-grade security features for professional mobility.",
        "Long Description (EN)": "The Dell Latitude 7390 represents the ultimate in business mobility, combining premium performance with enterprise-grade security in an ultra-portable design. This professional ultrabook features the powerful Intel Core i7-8650U quad-core processor, delivering exceptional performance for demanding business applications, data analysis, and multitasking scenarios. With 16GB of DDR4 memory and a fast 512GB SSD, this configuration provides excellent performance for professional workloads while maintaining quick access to files and applications. The 13.3-inch Full HD display with anti-glare coating ensures excellent visibility in any environment, while the premium keyboard and precision touchpad enhance productivity during long work sessions. Advanced security features include TPM 2.0, fingerprint reader, smart card reader, and optional IR camera for Windows Hello authentication. The durable carbon fiber construction meets MIL-STD-810G testing standards for reliability in challenging environments. This refurbished unit has been professionally restored to excellent condition, making it perfect for business professionals who need reliable performance and enterprise security in a portable form factor.",
        "Condition": "Refurbished (Excellent)",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i7",
        "Processor Model": "i7-8650U",
        "Processor Speed": "1.9 GHz",
        "Memory (RAM)": "16 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "512 GB",
        "Storage Type": "SSD",
        "Screen Size": "13.3 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel UHD Graphics 620",
        "Operating System": "Windows 10 Pro",
        "Weight": "2.87 lbs",
        "Color": "Black",
        "Image URL 1": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/latitude-notebooks/latitude-13-7390/media-gallery/latitude-7390-laptop-black-gallery-1.psd"
    })
    
    # Product 9: ThinkPad E590 i5 - 32GB RAM, 512GB SSD
    log_progress("Creating Product 9: ThinkPad E590 i5 - 512GB")
    products.append({
        "Shop sku": "TP-E590-32-512",
        "Title BB (EN)": "Lenovo ThinkPad E590 15.6\" Full HD Business Laptop - Intel Core i5-8265U, 32GB DDR4, 512GB SSD, Windows 10 Pro",
        "Brand Name": "Lenovo",
        "Model Number": "ThinkPad E590",
        "Short Description (EN)": "Reliable business laptop with legendary ThinkPad durability, 8th Gen Intel Core i5 processor, and professional features for small to medium businesses.",
        "Long Description (EN)": "The Lenovo ThinkPad E590 delivers the legendary reliability and performance that ThinkPad is known for, designed specifically for small to medium businesses and professional users. Powered by the efficient Intel Core i5-8265U quad-core processor, this laptop handles business applications, multitasking, and productivity tasks with confidence. The generous 32GB of DDR4 memory ensures smooth operation even with demanding applications, while the fast 512GB SSD provides quick boot times and responsive file access. The 15.6-inch Full HD IPS display offers excellent color accuracy and wide viewing angles, perfect for presentations and detailed work. The iconic ThinkPad keyboard provides the superior typing experience professionals demand, with excellent key travel and the famous TrackPoint pointing device. Enhanced security features include TPM 2.0, fingerprint reader, and Kensington lock slot for physical security. The durable construction and spill-resistant keyboard ensure reliable operation in demanding business environments. Perfect for professionals who need dependable performance and the trusted ThinkPad experience.",
        "Condition": "Brand New",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i5",
        "Processor Model": "i5-8265U",
        "Processor Speed": "1.6 GHz",
        "Memory (RAM)": "32 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "512 GB",
        "Storage Type": "SSD",
        "Screen Size": "15.6 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel UHD Graphics 620",
        "Operating System": "Windows 10 Pro",
        "Weight": "4.7 lbs",
        "Color": "Black",
        "Image URL 1": "https://p1-ofp.static.pub/medias/bWFzdGVyfHJvb3R8MjA4NTQ4fGltYWdlL3BuZ3xoNGYvaGQ4LzEwOTM4MjY2NjI0MDMwLnBuZ3w3YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5Yg/lenovo-laptop-thinkpad-e590-hero.png"
    })
    
    # Product 10: ThinkPad E590 i5 - 32GB RAM, 1TB SSD
    log_progress("Creating Product 10: ThinkPad E590 i5 - 1TB")
    products.append({
        "Shop sku": "TP-E590-32-1000",
        "Title BB (EN)": "Lenovo ThinkPad E590 15.6\" Full HD Business Laptop - Intel Core i5-8265U, 32GB DDR4, 1TB SSD, Windows 10 Pro",
        "Brand Name": "Lenovo",
        "Model Number": "ThinkPad E590",
        "Short Description (EN)": "Reliable business laptop with legendary ThinkPad durability, 8th Gen Intel Core i5 processor, and professional features for small to medium businesses.",
        "Long Description (EN)": "The Lenovo ThinkPad E590 delivers the legendary reliability and performance that ThinkPad is known for, designed specifically for small to medium businesses and professional users. Powered by the efficient Intel Core i5-8265U quad-core processor, this laptop handles business applications, multitasking, and productivity tasks with confidence. The generous 32GB of DDR4 memory ensures smooth operation even with demanding applications, while the spacious 1TB SSD provides extensive storage capacity with quick boot times and responsive file access. The 15.6-inch Full HD IPS display offers excellent color accuracy and wide viewing angles, perfect for presentations and detailed work. The iconic ThinkPad keyboard provides the superior typing experience professionals demand, with excellent key travel and the famous TrackPoint pointing device. Enhanced security features include TPM 2.0, fingerprint reader, and Kensington lock slot for physical security. The durable construction and spill-resistant keyboard ensure reliable operation in demanding business environments. Perfect for professionals who need dependable performance, extensive storage, and the trusted ThinkPad experience.",
        "Condition": "Brand New",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i5",
        "Processor Model": "i5-8265U",
        "Processor Speed": "1.6 GHz",
        "Memory (RAM)": "32 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "1 TB",
        "Storage Type": "SSD",
        "Screen Size": "15.6 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel UHD Graphics 620",
        "Operating System": "Windows 10 Pro",
        "Weight": "4.7 lbs",
        "Color": "Black",
        "Image URL 1": "https://p1-ofp.static.pub/medias/bWFzdGVyfHJvb3R8MjA4NTQ4fGltYWdlL3BuZ3xoNGYvaGQ4LzEwOTM4MjY2NjI0MDMwLnBuZ3w3YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5Yg/lenovo-laptop-thinkpad-e590-hero.png"
    })
    
    # Product 11: ThinkPad E590 i5 - 32GB RAM, 2TB SSD
    log_progress("Creating Product 11: ThinkPad E590 i5 - 2TB")
    products.append({
        "Shop sku": "TP-E590-32-2000",
        "Title BB (EN)": "Lenovo ThinkPad E590 15.6\" Full HD Business Laptop - Intel Core i5-8265U, 32GB DDR4, 2TB SSD, Windows 10 Pro",
        "Brand Name": "Lenovo",
        "Model Number": "ThinkPad E590",
        "Short Description (EN)": "Reliable business laptop with legendary ThinkPad durability, 8th Gen Intel Core i5 processor, and professional features for small to medium businesses.",
        "Long Description (EN)": "The Lenovo ThinkPad E590 delivers the legendary reliability and performance that ThinkPad is known for, designed specifically for small to medium businesses and professional users. Powered by the efficient Intel Core i5-8265U quad-core processor, this laptop handles business applications, multitasking, and productivity tasks with confidence. The generous 32GB of DDR4 memory ensures smooth operation even with demanding applications, while the massive 2TB SSD provides exceptional storage capacity with quick boot times and responsive file access for large datasets and media libraries. The 15.6-inch Full HD IPS display offers excellent color accuracy and wide viewing angles, perfect for presentations and detailed work. The iconic ThinkPad keyboard provides the superior typing experience professionals demand, with excellent key travel and the famous TrackPoint pointing device. Enhanced security features include TPM 2.0, fingerprint reader, and Kensington lock slot for physical security. The durable construction and spill-resistant keyboard ensure reliable operation in demanding business environments. Perfect for professionals who need dependable performance, maximum storage capacity, and the trusted ThinkPad experience.",
        "Condition": "Brand New",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i5",
        "Processor Model": "i5-8265U",
        "Processor Speed": "1.6 GHz",
        "Memory (RAM)": "32 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "2 TB",
        "Storage Type": "SSD",
        "Screen Size": "15.6 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel UHD Graphics 620",
        "Operating System": "Windows 10 Pro",
        "Weight": "4.7 lbs",
        "Color": "Black",
        "Image URL 1": "https://p1-ofp.static.pub/medias/bWFzdGVyfHJvb3R8MjA4NTQ4fGltYWdlL3BuZ3xoNGYvaGQ4LzEwOTM4MjY2NjI0MDMwLnBuZ3w3YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5Yg/lenovo-laptop-thinkpad-e590-hero.png"
    })
    
    # Product 12: ThinkPad E590 20nb001jus - 64GB RAM, 2TB SSD
    log_progress("Creating Product 12: ThinkPad E590 20nb001jus - 64GB/2TB")
    products.append({
        "Shop sku": "TP-E590-64-2000-001J",
        "Title BB (EN)": "Lenovo ThinkPad E590 20NB001JUS 15.6\" Full HD Business Laptop - Intel Core i5-8265U, 64GB DDR4, 2TB SSD, Windows 10 Pro",
        "Brand Name": "Lenovo",
        "Model Number": "20NB001JUS",
        "Short Description (EN)": "High-performance business laptop with legendary ThinkPad durability, maximum 64GB RAM configuration, and massive storage for demanding professional workloads.",
        "Long Description (EN)": "The Lenovo ThinkPad E590 20NB001JUS represents the ultimate configuration for demanding professional environments, combining the legendary ThinkPad reliability with maximum performance specifications. Powered by the efficient Intel Core i5-8265U quad-core processor, this laptop excels at intensive business applications, data analysis, and complex multitasking scenarios. The exceptional 64GB of DDR4 memory enables seamless operation of memory-intensive applications, virtual machines, and large datasets, while the massive 2TB SSD provides extensive storage capacity with enterprise-grade performance. The 15.6-inch Full HD IPS display delivers excellent color accuracy and wide viewing angles, essential for professional presentations and detailed analytical work. The iconic ThinkPad keyboard provides the superior typing experience that professionals demand, featuring excellent key travel, precise feedback, and the famous TrackPoint pointing device for enhanced productivity. Advanced security features include TPM 2.0, fingerprint reader, and Kensington lock slot for comprehensive data protection. The military-grade construction and spill-resistant keyboard ensure reliable operation in the most demanding business environments. Perfect for power users, data analysts, and professionals who require maximum performance and storage capacity.",
        "Condition": "Brand New",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i5",
        "Processor Model": "i5-8265U",
        "Processor Speed": "1.6 GHz",
        "Memory (RAM)": "64 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "2 TB",
        "Storage Type": "SSD",
        "Screen Size": "15.6 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel UHD Graphics 620",
        "Operating System": "Windows 10 Pro",
        "Weight": "4.7 lbs",
        "Color": "Black",
        "Image URL 1": "https://p1-ofp.static.pub/medias/bWFzdGVyfHJvb3R8MjA4NTQ4fGltYWdlL3BuZ3xoNGYvaGQ4LzEwOTM4MjY2NjI0MDMwLnBuZ3w3YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5Yg/lenovo-laptop-thinkpad-e590-hero.png"
    })
    
    # Product 13: ThinkPad E590 20nb001jus - 32GB RAM, 1TB SSD
    log_progress("Creating Product 13: ThinkPad E590 20nb001jus - 32GB/1TB")
    products.append({
        "Shop sku": "TP-E590-32-1000-001J",
        "Title BB (EN)": "Lenovo ThinkPad E590 20NB001JUS 15.6\" Full HD Business Laptop - Intel Core i5-8265U, 32GB DDR4, 1TB SSD, Windows 10 Pro",
        "Brand Name": "Lenovo",
        "Model Number": "20NB001JUS",
        "Short Description (EN)": "Professional business laptop with legendary ThinkPad durability, high-performance 32GB RAM configuration, and ample storage for business productivity.",
        "Long Description (EN)": "The Lenovo ThinkPad E590 20NB001JUS delivers exceptional business performance with the trusted ThinkPad reliability that professionals depend on. Powered by the efficient Intel Core i5-8265U quad-core processor, this laptop handles demanding business applications, multitasking, and productivity workflows with confidence. The substantial 32GB of DDR4 memory ensures smooth operation of complex applications and enables efficient multitasking across multiple programs, while the spacious 1TB SSD provides ample storage with fast access times for documents, applications, and media files. The 15.6-inch Full HD IPS display offers excellent color reproduction and wide viewing angles, perfect for presentations, detailed work, and collaboration. The legendary ThinkPad keyboard delivers the superior typing experience that business professionals demand, featuring precise key travel, excellent tactile feedback, and the iconic TrackPoint pointing device for enhanced navigation. Comprehensive security features include TPM 2.0, fingerprint reader, and Kensington lock slot for data protection and physical security. The durable construction and spill-resistant design ensure reliable operation in challenging business environments. Ideal for business professionals, consultants, and mobile workers who need dependable performance and the trusted ThinkPad experience.",
        "Condition": "Brand New",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i5",
        "Processor Model": "i5-8265U",
        "Processor Speed": "1.6 GHz",
        "Memory (RAM)": "32 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "1 TB",
        "Storage Type": "SSD",
        "Screen Size": "15.6 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel UHD Graphics 620",
        "Operating System": "Windows 10 Pro",
        "Weight": "4.7 lbs",
        "Color": "Black",
        "Image URL 1": "https://p1-ofp.static.pub/medias/bWFzdGVyfHJvb3R8MjA4NTQ4fGltYWdlL3BuZ3xoNGYvaGQ4LzEwOTM4MjY2NjI0MDMwLnBuZ3w3YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5YjE5Yg/lenovo-laptop-thinkpad-e590-hero.png"
    })
    
    # Product 14: HP Pavilion 15 ER-0008ca - 32GB RAM
    log_progress("Creating Product 14: HP Pavilion 15 ER-0008ca")
    products.append({
        "Shop sku": "HP-PAV15-32-1000-ER",
        "Title BB (EN)": "HP Pavilion 15 ER-0008ca 15.6\" Full HD Laptop - Intel Core i5-1235U, 32GB DDR4, 1TB SSD, Intel Iris Xe Graphics, Windows 11 Home",
        "Brand Name": "HP",
        "Model Number": "ER-0008ca",
        "Short Description (EN)": "Stylish and versatile 15.6-inch laptop with 12th Gen Intel Core i5 processor, generous 32GB RAM, and modern features for everyday computing and entertainment.",
        "Long Description (EN)": "The HP Pavilion 15 ER-0008ca combines style, performance, and value in a sleek design perfect for everyday computing, entertainment, and productivity tasks. Powered by the modern 12th Generation Intel Core i5-1235U processor with Intel Iris Xe graphics, this laptop delivers smooth performance for web browsing, office applications, content consumption, and light creative work. The generous 32GB of DDR4 memory ensures excellent multitasking capabilities, allowing you to run multiple applications simultaneously without slowdown, while the spacious 1TB SSD provides ample storage with fast boot times and quick file access. The 15.6-inch Full HD display offers vibrant colors and sharp detail for an enjoyable viewing experience, whether you're working on documents, streaming videos, or browsing the web. The modern design features a comfortable keyboard and precision touchpad for efficient navigation and typing. Contemporary connectivity options including USB-C, USB-A ports, HDMI, and Wi-Fi 6 ensure compatibility with current and future devices. The sleek profile and attractive finish make this laptop suitable for both professional and personal use. Perfect for students, home users, and professionals who need reliable performance and modern features at an excellent value.",
        "Condition": "Brand New",
        "Category Code": "BB_36711",
        "Processor Type": "Intel Core i5",
        "Processor Model": "i5-1235U",
        "Processor Speed": "1.3 GHz",
        "Memory (RAM)": "32 GB",
        "Memory Type": "DDR4",
        "Storage Capacity": "1 TB",
        "Storage Type": "SSD",
        "Screen Size": "15.6 inches",
        "Screen Resolution": "1920 x 1080",
        "Touchscreen": "No",
        "Graphics": "Intel Iris Xe Graphics",
        "Operating System": "Windows 11 Home",
        "Weight": "3.86 lbs",
        "Color": "Natural Silver",
        "Image URL 1": "https://ssl-product-images.www8-hp.com/digmedialib/prodimg/lowres/c08049292.png"
    })
    
    log_progress(f"✅ Created all {len(products)} products successfully!")
    return products

def generate_excel_template():
    """Generate the Excel template"""
    log_progress("📊 Generating Excel template...")
    
    products = create_all_products()
    
    # Create DataFrame
    df = pd.DataFrame(products)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"professional_bestbuy_listings_{timestamp}.xlsx"
    
    log_progress(f"💾 Saving to file: {filename}")
    
    # Create Excel file
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        # Main data sheet
        df.to_excel(writer, sheet_name='Data', index=False)
        
        # Reference data sheet (required by Best Buy)
        pd.DataFrame().to_excel(writer, sheet_name='ReferenceData', index=False)
        
        # Columns sheet
        columns_info = pd.DataFrame({
            'Column Name': df.columns.tolist(),
            'Data Type': ['Text'] * len(df.columns),
            'Required': ['Yes'] * len(df.columns)
        })
        columns_info.to_excel(writer, sheet_name='Columns', index=False)
    
    log_progress(f"🎉 TEMPLATE GENERATED SUCCESSFULLY!")
    log_progress(f"📁 File: {filename}")
    log_progress(f"📊 Products: {len(products)}")
    log_progress(f"📋 Fields: {len(df.columns)}")
    
    return filename

def monitor_execution():
    """Monitor the execution with live updates"""
    log_progress("🚀 STARTING BEST BUY TEMPLATE GENERATION WITH LIVE MONITORING")
    
    try:
        filename = generate_excel_template()
        log_progress(f"✅ SUCCESS! Template saved as: {filename}")
        return filename
    except Exception as e:
        log_progress(f"❌ ERROR: {str(e)}")
        raise

if __name__ == "__main__":
    monitor_execution()

