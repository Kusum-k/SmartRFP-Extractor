import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY', 'your-api-key-here')
        self.openai_model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
        self.target_fields = [
            "bid_number", "title", "due_date", "bid_submission_type",
            "term_of_bid", "pre_bid_meeting", "installation", 
            "bid_bond_requirement", "delivery_date", "payment_terms",
            "additional_documentation_required", "mfg_for_registration",
            "contract_or_cooperative_to_use", "model_no", "part_no",
            "product", "contact_info", "company_name", "bid_summary",
            "product_specification"
        ]
        
        # Processing settings
        self.max_text_length = 8000
        self.temperature = 0.1
        self.max_tokens = 1500
        
        # File paths
        self.input_folder = 'sample_documents'
        self.output_folder = 'output'
        
        # Supported file formats
        self.supported_formats = ['.pdf', '.html', '.htm']
        
        # Validation patterns
        self.validation_patterns = {
            'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'phone': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            'date': r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',
            'bid_number': r'[A-Z]{2,}-?\d{5,}'
        }
        
        # Logging settings
        self.log_level = 'INFO'
        self.log_file = 'rfp_processor.log'
        
        # Retry settings for API calls
        self.max_retries = 3
        self.retry_delay = 2  # seconds
        
    def validate(self):
        if not self.openai_api_key or self.openai_api_key == 'your-api-key-here':
            raise ValueError("OpenAI API key not configured. Please set OPENAI_API_KEY in .env file")
        
        # Create necessary directories
        os.makedirs(self.input_folder, exist_ok=True)
        os.makedirs(self.output_folder, exist_ok=True)
        
        return True
    
    def get_field_description(self, field_name):
        descriptions = {
            "bid_number": "RFP/Bid identification number",
            "title": "Document title or project name",
            "due_date": "Proposal submission deadline",
            "bid_submission_type": "Method of submission (electronic, mail, etc.)",
            "term_of_bid": "Contract duration or term length",
            "pre_bid_meeting": "Pre-bid meeting date and details",
            "installation": "Installation requirements or services",
            "bid_bond_requirement": "Required bid bond or guarantee",
            "delivery_date": "Expected delivery date",
            "payment_terms": "Payment conditions and terms",
            "additional_documentation_required": "Extra documents needed",
            "mfg_for_registration": "Manufacturer registration requirements",
            "contract_or_cooperative_to_use": "Contract type or cooperative agreement",
            "model_no": "Product model number",
            "part_no": "Product part number",
            "product": "Product description",
            "contact_info": "Contact person and details",
            "company_name": "Issuing organization name",
            "bid_summary": "Brief summary of the bid",
            "product_specification": "Technical specifications"
        }
        return descriptions.get(field_name, field_name)
