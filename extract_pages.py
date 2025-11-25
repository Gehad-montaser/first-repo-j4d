#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PyPDF2
import sys

def extract_pages(pdf_path, start_page, end_page):
    """Extract text from specific pages of a PDF"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)
            
            print(f"إجمالي عدد الصفحات في الملف: {total_pages}")
            print(f"استخراج الصفحات من {start_page} إلى {end_page}\n")
            print("="*80)
            
            # Adjust for 0-based indexing
            start_idx = start_page - 1
            end_idx = min(end_page, total_pages)
            
            all_text = []
            
            for page_num in range(start_idx, end_idx):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                
                print(f"\n{'='*80}")
                print(f"صفحة {page_num + 1}")
                print(f"{'='*80}")
                print(text)
                
                all_text.append(f"\n--- صفحة {page_num + 1} ---\n{text}")
            
            # Save to file
            output_file = '/vercel/sandbox/extracted_content.txt'
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(all_text))
            
            print(f"\n\n{'='*80}")
            print(f"تم حفظ المحتوى في: {output_file}")
            print(f"{'='*80}")
            
    except Exception as e:
        print(f"خطأ: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    pdf_path = "/vercel/sandbox/uploads/منهج الفرقه الاولي -اللغة الالمانية.pdf"
    extract_pages(pdf_path, 12, 40)
