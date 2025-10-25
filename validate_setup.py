"""
Validate that the RFP processor is set up correctly
"""

import os
import sys

def validate_setup():
    """Check if all requirements are met"""
    
    print("Validating RFP Processor Setup...")
    print("-" * 50)
    
    issues = []
    
    # Check Python version
    if sys.version_info < (3, 8):
        issues.append("Python 3.8+ required")
    else:
        print("✓ Python version OK")
    
    # Check required files
    required_files = [
        'main.py',
        'config.py',
        'document_parser.py',
        'field_extractor.py',
        'output_generator.py',
        'requirements.txt'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} found")
        else:
            issues.append(f"Missing file: {file}")
    
    # Check directories
    required_dirs = ['sample_documents', 'output']
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✓ {dir_name}/ directory found")
        else:
            os.makedirs(dir_name, exist_ok=True)
            print(f"✓ Created {dir_name}/ directory")
    
    # Check .env file
    if os.path.exists('.env'):
        print("✓ .env file found")
        
        # Check if API key is set
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key and api_key != 'your-api-key-here':
            print("✓ OpenAI API key configured")
        else:
            issues.append("OpenAI API key not configured in .env")
    else:
        issues.append("Missing .env file")
    
    # Check dependencies
    try:
        import openai
        import PyPDF2
        import bs4
        print("✓ All dependencies installed")
    except ImportError as e:
        issues.append(f"Missing dependency: {e}")
    
    # Summary
    print("-" * 50)
    if issues:
        print("\n❌ Setup Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nPlease fix these issues before running the processor.")
        return False
    else:
        print("\n✅ Setup validation passed!")
        print("You're ready to process RFP documents!")
        return True

if __name__ == "__main__":
    validate_setup()
