# import os
# # import textract
# from PyPDF2 import PdfReader
# import pdfplumber
# from pymongo import MongoClient

# # from summarization import summarize_text

# from src.summarization import summarize_text
# from src.keyword_extraction import extract_keywords

# # from keyword_extraction import extract_keywords

# # Initialize MongoDB connection
# client = MongoClient("mongodb://localhost:27017/")
# db = client["pdf_summary_db"]
# collection = db["pdf_documents"]

# # Define the base directory containing the PDFs
# base_dir = 'pdfs/'

# # Function to read PDFs using pdfplumber for better accuracy
# def read_pdf(file):
#     try:
#         with pdfplumber.open(file) as pdf:
#             text = ''
#             for page in pdf.pages:
#                 text += page.extract_text() if page.extract_text() else ''
#         return text
#     except Exception as e:
#         print(f'Error reading PDF {file}: {e}')
#         return None

# # Walk through the directory structure and process PDFs
# for root, dirs, files in os.walk(base_dir):
#     for file_name in files:
#         # Print the file name for debugging purposes
#         print(f'Processing file: {file_name}')
        
#         # Get the file path
#         file_path = os.path.join(root, file_name)
        
#         # Handle only PDFs in this case
#         if file_name.endswith('.pdf'):
#             content = read_pdf(file_path)
#         else:
#             print(f'Skipping file: {file_name} (unsupported format)')
#             continue
        
#         if content is not None:
#             # Summarize the text
#             summary = summarize_text(content, method="textrank")  # You can use the transformer-based method here
            
#             # Extract keywords from the text
#             keywords = extract_keywords(content, num_keywords=5)
            
#             # Store the results in MongoDB
#             document = {
#                 "pdf_name": file_name,
#                 "summary": summary,
#                 "keywords": keywords
#             }
#             collection.insert_one(document)
#             print(f'Successfully processed and saved {file_name}')
#         else:
#             print(f'Failed to read file {file_name}. Content is None.')

# print('PDF processing complete, summaries and keywords saved to MongoDB successfully!')


import os
import pdfplumber
from src.summarization import summarize_text
from src.keyword_extraction import extract_keywords
from src.db_operations import connect_to_mongo, store_pdf_data

# Initialize MongoDB connection
db = connect_to_mongo()

# Directory containing PDFs
pdf_dir = 'pdfs'

def process_pdf(file_name, file_path):
    """
    Process a single PDF file: extract text, summarize, extract keywords, and store in MongoDB.
    """
    print(f"Processing file: {file_name}")
    
    # Extract text from PDF
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''

    if text:
        # Summarize the text using TextRank
        summary = summarize_text(text, method="textrank")
        
        # Extract keywords using TF-IDF (or YAKE)
        keywords = extract_keywords(text, num_keywords=5)
        
        # Store results in MongoDB
        store_pdf_data(db, file_name, summary, keywords)
        print(f"Successfully processed and stored {file_name}")
    else:
        print(f"No text extracted from {file_name}")

# Process all PDFs in the directory
def process_all_pdfs(pdf_dir):
    """
    Process all PDFs in the specified directory.
    """
    for root, dirs, files in os.walk(pdf_dir):
        for file_name in files:
            if file_name.endswith('.pdf'):
                file_path = os.path.join(root, file_name)
                process_pdf(file_name, file_path)

if __name__ == "__main__":
    # Process all PDFs in the directory
    process_all_pdfs(pdf_dir)
    print("All PDFs processed successfully!")
