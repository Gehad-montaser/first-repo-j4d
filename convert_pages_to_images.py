#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fitz  # PyMuPDF
import sys

def convert_pages_to_images(pdf_path, start_page, end_page, output_dir="/vercel/sandbox/pages"):
    """Convert PDF pages to high-quality images"""
    try:
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        
        print(f"إجمالي عدد الصفحات في الملف: {total_pages}")
        print(f"تحويل الصفحات من {start_page} إلى {end_page} إلى صور\n")
        print("="*80)
        
        # Adjust for 0-based indexing
        start_idx = start_page - 1
        end_idx = min(end_page, total_pages)
        
        saved_pages = []
        
        for page_num in range(start_idx, end_idx):
            page = doc[page_num]
            
            # Render page to an image with high resolution
            mat = fitz.Matrix(2.0, 2.0)  # 2x zoom for better quality
            pix = page.get_pixmap(matrix=mat)
            
            # Save as PNG
            output_file = f"{output_dir}/page_{page_num + 1:03d}.png"
            pix.save(output_file)
            
            saved_pages.append(output_file)
            print(f"✓ تم حفظ صفحة {page_num + 1}: {output_file}")
        
        print(f"\n{'='*80}")
        print(f"تم حفظ {len(saved_pages)} صفحة في المجلد: {output_dir}")
        print(f"{'='*80}\n")
        
        # Create an index file
        index_file = f"{output_dir}/index.txt"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(f"الصفحات المحفوظة من {start_page} إلى {end_page-1}\n")
            f.write("="*80 + "\n\n")
            for page_file in saved_pages:
                f.write(f"{page_file}\n")
        
        print(f"تم إنشاء ملف الفهرس: {index_file}\n")
        
        doc.close()
        
    except Exception as e:
        print(f"خطأ: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    pdf_path = "/vercel/sandbox/uploads/منهج الفرقه الاولي -اللغة الالمانية.pdf"
    convert_pages_to_images(pdf_path, 12, 40)
