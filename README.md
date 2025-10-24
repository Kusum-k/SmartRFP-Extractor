# RFP Document Processing System

A Python program that extracts structured information from RFP documents (PDF and HTML) and outputs the data in JSON format.

## Features
- Parses PDF and HTML documents
- Extracts key RFP information using OpenAI GPT
- Validates extracted data
- Outputs structured JSON

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Set your OpenAI API key in config.py
3. Run: `python main.py`

## Usage
```python
from main import RFPProcessor

processor = RFPProcessor()
results = processor.process_documents(['document.pdf'])
processor.save_results(results, 'output.json')
