import json
import os
from datetime import datetime
from document_parser import DocumentParser
from field_extractor import FieldExtractor
from output_generator import OutputGenerator
from config import Config

class RFPProcessor:
    def __init__(self):
        self.config = Config()
        self.parser = DocumentParser()
        self.extractor = FieldExtractor(self.config.openai_api_key)
        self.output_gen = OutputGenerator()
        
    def process_documents(self, file_paths):
        results = {}
        
        print("Starting RFP document processing...")
        
        for file_path in file_paths:
            print(f"Processing: {file_path}")
            
            # Parse document
            content = self.parser.parse_document(file_path)
            
            # Extract fields
            extracted_data = self.extractor.extract_fields(content)
            
            # Store results
            results[file_path] = {
                'extracted_fields': extracted_data,
                'processed_at': datetime.now().isoformat(),
                'source_file': file_path
            }
            
        print(f"Completed processing {len(file_paths)} documents")
        return results
    
    def save_results(self, results, output_path):
        """Save results to JSON file"""
        self.output_gen.save_to_json(results, output_path)
        print(f"Results saved to: {output_path}")

def main():
    # Example usage
    processor = RFPProcessor()
    
    # Process the uploaded documents
    documents = [
        'sample_documents/dallas_isd_addendum1.pdf',
        'sample_documents/dallas_isd_addendum2.pdf',
        'sample_documents/maryland_porfp.pdf'
    ]
    
    # Process documents
    results = processor.process_documents(documents)
    
    # Save results
    processor.save_results(results, 'output/extracted_data.json')

if __name__ == "__main__":
    main()
