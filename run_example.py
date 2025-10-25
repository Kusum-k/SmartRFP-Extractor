from main import RFPProcessor
import os

def run_example():
     print("=" * 50)
    print("RFP Document Processor - Example")
    print("=" * 50)
    
    # Initialize processor
    processor = RFPProcessor()
    
    # Example documents (update paths as needed)
    example_docs = [
        'sample_documents/example_rfp.pdf'
    ]
    
    # Check if files exist
    existing_files = [f for f in example_docs if os.path.exists(f)]
    
    if not existing_files:
        print("\nNo example documents found!")
        print("Please add PDF files to the 'sample_documents/' folder")
        return
    
    print(f"\nProcessing {len(existing_files)} document(s)...")
    
    # Process documents
    results = processor.process_documents(existing_files)
    
    # Save results
    output_file = 'output/example_results.json'
    processor.save_results(results, output_file)
    
    print("\n" + "=" * 50)
    print("Example completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    run_example()
