#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fitz  # PyMuPDF
import sys

def extract_pages_with_images(pdf_path, start_page, end_page):
    """Extract text and images from specific pages of a PDF using PyMuPDF"""
    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        
        print(f"إجمالي عدد الصفحات في الملف: {total_pages}")
        print(f"استخراج الصفحات من {start_page} إلى {end_page}\n")
        print("="*80)
        
        # Adjust for 0-based indexing
        start_idx = start_page - 1
        end_idx = min(end_page, total_pages)
        
        all_content = []
        
        for page_num in range(start_idx, end_idx):
            page = doc[page_num]
            
            # Extract text
            text = page.get_text()
            
            # Get images on the page
            image_list = page.get_images()
            
            print(f"\n{'='*80}")
            print(f"صفحة {page_num + 1}")
            print(f"{'='*80}")
            
            if text.strip():
                print(f"النص:\n{text}")
            else:
                print("لا يوجد نص قابل للاستخراج")
            
            if image_list:
                print(f"\nعدد الصور في هذه الصفحة: {len(image_list)}")
                
                # Save images
                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    
                    image_filename = f"/vercel/sandbox/page_{page_num + 1}_img_{img_index + 1}.{image_ext}"
                    with open(image_filename, "wb") as img_file:
                        img_file.write(image_bytes)
                    print(f"  - تم حفظ الصورة: {image_filename}")
            
            content_entry = f"\n--- صفحة {page_num + 1} ---\n"
            if text.strip():
                content_entry += f"النص:\n{text}\n"
            if image_list:
                content_entry += f"عدد الصور: {len(image_list)}\n"
            
            all_content.append(content_entry)
        
        # Save to file
        output_file = '/vercel/sandbox/extracted_content_detailed.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(all_content))
        
        print(f"\n\n{'='*80}")
        print(f"تم حفظ المحتوى في: {output_file}")
        print(f"{'='*80}")
        
        doc.close()
        
    except Exception as e:
        print(f"خطأ: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    pdf_path = "/vercel/sandbox/uploads/منهج الفرقه الاولي -اللغة الالمانية.pdf"
    extract_pages_with_images(pdf_path, 12, 40)
