import openai
import json
import re

class FieldExtractor:
    def __init__(self, api_key):
        openai.api_key = api_key
                self.client = openai.OpenAI(api_key=api_key)
    
    def extract_fields(self, document_content):
        
        text = document_content.get('text', '')
        if not text:
            return self._get_empty_fields()
        if len(text) > 8000:
            text = text[:8000] + "..."
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self._get_system_prompt()},
                    {"role": "user", "content": f"Extract information from this document:\n\n{text}"}
                ],
                temperature=0.1,
                max_tokens=1500
            )
            
            # Parse the response
            content = response.choices[0].message.content
            extracted_data = self._parse_gpt_response(content)
            
            return extracted_data
            
        except Exception as e:
            print(f"Error with OpenAI API: {e}")
            return self._get_empty_fields()
    
    def _get_system_prompt(self):
        return """You are helping extract information from RFP documents. 
        
Extract the following information and return it as JSON:
- bid_number: The RFP/bid number
- title: Document title
- due_date: When proposals are due
- bid_submission_type: How to submit (electronic, mail, etc.)
- term_of_bid: Contract length/term
- pre_bid_meeting: Pre-bid meeting info
- installation: Installation requirements
- bid_bond_requirement: Bond requirements
- delivery_date: When delivery is needed
- payment_terms: Payment conditions
- additional_documentation_required: Extra docs needed
- mfg_for_registration: Manufacturer registration info
- contract_or_cooperative_to_use: Contract type
- model_no: Product model numbers
- part_no: Part numbers
- product: Product description
- contact_info: Contact details
- company_name: Issuing company/organization
- bid_summary: Brief summary
- product_specification: Technical specs
    
    def _parse_gpt_response(self, content):
        try:
            # Try to find JSON in the response
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            
            if json_start != -1 and json_end != -1:
                json_str = content[json_start:json_end]
                return json.loads(json_str)
            else:
                # Fallback: try to parse the whole content
                return json.loads(content)
                
        except json.JSONDecodeError:
            print("Failed to parse JSON from GPT response")
            return self._extract_with_regex(content)
    
    def _extract_with_regex(self, content):
        fields = self._get_empty_fields()
        
        # Simple regex patterns for common fields
        patterns = {
            'bid_number': r'(?:RFP|Bid|PORFP)[\s#:]*([A-Z0-9\-]+)',
            'due_date': r'due[\s\w]*date[:\s]*([^\n]+)',
            'company_name': r'(?:company|organization)[:\s]*([^\n]+)',
            'contact_info': r'contact[:\s]*([^\n]+)'
        }
        
        for field, pattern in patterns.items():
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                fields[field] = match.group(1).strip()
        
        return fields
    
    def _get_empty_fields(self):
        return {
            "bid_number": None,
            "title": None,
            "due_date": None,
            "bid_submission_type": None,
            "term_of_bid": None,
            "pre_bid_meeting": None,
            "installation": None,
            "bid_bond_requirement": None,
            "delivery_date": None,
            "payment_terms": None,
            "additional_documentation_required": None,
            "mfg_for_registration": None,
            "contract_or_cooperative_to_use": None,
            "model_no": None,
            "part_no": None,
            "product": None,
            "contact_info": None,
            "company_name": None,
            "bid_summary": None,
            "product_specification": None
        }
