"""
Generate JSON output from extracted data
"""

import json
import os
from datetime import datetime

class OutputGenerator:
    def __init__(self):
        pass
    
    def save_to_json(self, results, output_path):
        """Save results to JSON file"""
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Prepare output data
        output_data = {
            "metadata": {
                "processed_at": datetime.now().isoformat(),
                "total_documents": len(results),
                "system_info": "RFP Document Processing System v1.0"
            },
            "documents": {}
        }
        
        # Process each document result
        for file_path, result in results.items():
            doc_name = os.path.basename(file_path)
            
            output_data["documents"][doc_name] = {
                "source_file": file_path,
                "processed_at": result.get("processed_at"),
                "extracted_fields": result.get("extracted_fields", {}),
                "field_count": len([v for v in result.get("extracted_fields", {}).values() if v is not None])
            }
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"JSON output saved to: {output_path}")
    
    def generate_summary_report(self, results):
        """Generate a summary report of extraction results"""
        total_docs = len(results)
        total_fields = 0
        extracted_fields = 0
        
        for result in results.values():
            fields = result.get("extracted_fields", {})
            total_fields += len(fields)
            extracted_fields += len([v for v in fields.values() if v is not None])
        
        completion_rate = (extracted_fields / total_fields * 100) if total_fields > 0 else 0
        
        return {
            "total_documents": total_docs,
            "total_fields": total_fields,
            "extracted_fields": extracted_fields,
            "completion_rate": f"{completion_rate:.1f}%"
        }
