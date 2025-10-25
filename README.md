#  SmartRFP Extractor

A Python-based application that automatically extracts **structured information** from **Request for Proposal (RFP)** documents in **PDF** and **HTML** formats, and exports the extracted data in **JSON** format.

##  Features

-  **Multi-format Support** — Parses both PDF and HTML documents.  
-  **Smart Extraction** — Uses **OpenAI GPT models** to extract key RFP information such as Bid Number, Title, Due Date, Product   Specifications, etc.  
-  **Validation Layer** — Ensures extracted data is properly structured and mapped to predefined fields.  
-  **JSON Output** — Exports all extracted information into a clean and organized JSON file.  
-  **Configurable Setup** — API key, model, and processing options are defined in `config.py`.  

##  Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

 2.**Configure API Key**

   Open the .env file or config.py and set your OpenAI API key:
   OPENAI_API_KEY=your_api_key_here

 3.**Run the Program**
   
   python main.py

   ## Usage Example
   from main import RFPProcessor

   # Initialize the processor
   processor = RFPProcessor()

   # Process your RFP documents
   results = processor.process_documents(['sample_documents/document.pdf'])

   # Save results as JSON
   processor.save_results(results, 'output/extracted_data.json')

   ## Output Format
   {
  "metadata": {
    "processed_at": "2025-10-25T12:30:10",
    "total_documents": 1,
    "system_info": "RFP Document Processing System v1.0"
  },
  "documents": {
    "document.pdf": {
      "source_file": "sample_documents/document.pdf",
      "extracted_fields": {
        "bid_number": "JA-207652",
        "title": "Student and Staff Computing Devices",
        "due_date": "July 9, 2024",
        "company_name": "Dallas Independent School District"
      },
      "field_count": 4
    }
  }
}


