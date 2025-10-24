"""
Document parser for PDF and HTML files
"""

import PyPDF2
from bs4 import BeautifulSoup
import os

class DocumentParser:
    def __init__(self):
        pass
    
    def parse_document(self, file_path):
        """Parse document based on file extension"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        file_ext = os.path.splitext(file_path)[1].lower()
        
        if file_ext == '.pdf':
            return self.parse_pdf(file_path)
        elif file_ext in ['.html', '.htm']:
            return self.parse_html(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_ext}")
    
    def parse_pdf(self, file_path):
        """Extract text from PDF file"""
        text_content = []
        
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                for page in pdf_reader.pages:
                    text_content.append(page.extract_text())
            
            return {
                'text': '\n\n'.join(text_content),
                'page_count': len(pdf_reader.pages),
                'file_type': 'pdf'
            }
            
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return {'text': '', 'error': str(e)}
    
    def parse_html(self, file_path):
        """Extract text from HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file.read(), 'html.parser')
                
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()
                
                text = soup.get_text()
                
                # Clean up text
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                text = ' '.join(chunk for chunk in chunks if chunk)
                
                return {
                    'text': text,
                    'file_type': 'html'
                }
                
        except Exception as e:
            print(f"Error parsing HTML: {e}")
            return {'text': '', 'error': str(e)}
