#!/usr/bin/env python3
import sys
import pdfplumber
import argparse
import re

def search_pdf(pdf_path, search_term):
    """
    Search for a term in a PDF and extract the row containing it.
    Specially designed for medical procedure tables.
    """
    print(f"Searching for '{search_term}' in {pdf_path}...")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            found = False
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text and search_term.lower() in text.lower():
                    print(f"\n--- Found on Page {i+1} ---")
                    
                    # Try to extract tables first
                    tables = page.extract_tables()
                    if tables:
                        for table in tables:
                            for row in table:
                                # Clean row of None values
                                clean_row = [str(cell).replace('\n', ' ') if cell else "" for cell in row]
                                row_text = " | ".join(clean_row)
                                
                                if search_term.lower() in row_text.lower():
                                    print(f"Match: {row_text}")
                                    found = True
                    
                    # If no tables or term not in tables, print lines
                    if not found:
                        lines = text.split('\n')
                        for line in lines:
                            if search_term.lower() in line.lower():
                                print(f"Match (text): {line}")
                                found = True
            
            if not found:
                print(f"Term '{search_term}' not found in the document.")
                
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search for medical procedures in PDF tables')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('search_term', help='Term to search for (code or name)')
    
    args = parser.parse_args()
    search_pdf(args.pdf_path, args.search_term)
