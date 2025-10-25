"""
Document parser for PDF and HTML files
"""

import PyPDF2
from bs4 import BeautifulSoup
import os

class DocumentParser:
    def __init__(self):
        self.supported_formats = ['.pdf', '.html', '.htm']
    
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
                
                # Extract text from each page
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text:
                        text_content.append(text)
            
            full_text = '\n\n'.join(text_content)
            
            return {
                'text': full_text,
                'page_count': len(pdf_reader.pages),
                'file_type': 'pdf',
                'file_name': os.path.basename(file_path)
            }
            
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return {
                'text': '', 
                'error': str(e), 
                'file_type': 'pdf',
                'file_name': os.path.basename(file_path)
            }
    
    def parse_html(self, file_path):
        """Extract text from HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file.read(), 'html.parser')
                
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()
                
                # Get text
                text = soup.get_text()
                
                # Clean up whitespace
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                clean_text = ' '.join(chunk for chunk in chunks if chunk)
                
                return {
                    'text': clean_text,
                    'file_type': 'html',
                    'file_name': os.path.basename(file_path)
                }
                
        except Exception as e:
            print(f"Error parsing HTML: {e}")
            return {
                'text': '', 
                'error': str(e), 
                'file_type': 'html',
                'file_name': os.path.basename(file_path)
            }
    
    def is_supported_format(self, file_path):
        """Check if file format is supported"""
        file_ext = os.path.splitext(file_path)[1].lower()
        return file_ext in self.supported_formats
    
    def get_file_info(self, file_path):
        """Get basic file information"""
        if not os.path.exists(file_path):
            return None
        
        return {
            'file_name': os.path.basename(file_path),
            'file_size': os.path.getsize(file_path),
            'file_extension': os.path.splitext(file_path)[1],
            'full_path': os.path.abspath(file_path)
        }
