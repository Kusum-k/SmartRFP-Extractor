# Usage Guide

## Quick Start

1. **Setup**
      pip install -r requirements.txt

2. Configure API Key
     Create a .env file
     Add: OPENAI_API_KEY=your_key_here
   
3.Add Documents
     Place PDF/HTML files in sample_documents/ folder
     
4.Run
     python main.py
     
5.Check Results
     Results saved in output/extracted_data.json
Example:
from main import RFPProcessor

# Initialize
processor = RFPProcessor()

# Process documents
results = processor.process_documents([
    'sample_documents/rfp_document.pdf'
])

# Save results
processor.save_results(results, 'output/results.json')
