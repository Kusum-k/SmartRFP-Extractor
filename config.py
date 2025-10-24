"""
Configuration settings for RFP processor
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY', 'your-api-key-here')
        
        # Target fields to extract
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
