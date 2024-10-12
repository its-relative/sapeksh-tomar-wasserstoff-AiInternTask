# import os
# import requests
# import pdfplumber
from transformers import pipeline  # Import necessary for summarization

# from src.summarization import generate_summary_for_pdf_text  # Corrected import
# from src.keyword_extraction import extract_keywords_from_pdf_text  # Corrected import
# from src.db_operations import connect_to_mongo, store_pdf_data  # Comment out MongoDB operations

# Directory for downloading PDFs
# download_dir = 'downloaded_pdfs'

# Summarizer class for Hugging Face transformer-based summarization
class Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        # Load a pre-trained summarization model from Hugging Face
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text, max_length=130, min_length=30):
        try:
            # Generate a summary for the provided text
            summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            print(f"Error during summarization: {e}")
            return None

# Test the summarizer directly with simple text
if __name__ == "__main__":
    # Test input
    simple_text = "This is a test document. It contains some text to be summarized using a transformer-based model."
    summary = Summarizer().summarize(simple_text, max_length=50, min_length=10)
    
    # Print the summary
    print(summary)

# Comment out the sections below for now, as we are focusing on testing summarization

# # Ensure download directory exists
# if not os.path.exists(download_dir):
#     os.makedirs(download_dir)

# def download_pdf(pdf_name, url):
#     """
#     Download PDF from a given URL and save it to the download directory.
#     """
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             file_path = os.path.join(download_dir, f"{pdf_name}.pdf")
#             with open(file_path, 'wb') as f:
#                 f.write(response.content)
#             print(f"{pdf_name} downloaded successfully.")
#             return file_path
#         else:
#             print(f"Failed to download {pdf_name}. Status code: {response.status_code}")
#             return None
#     except Exception as e:
#         print(f"Error downloading {pdf_name}: {e}")
#         return None

# def process_pdf(file_name, file_path):
#     """
#     Process a single PDF file: extract text, summarize, extract keywords, and store in MongoDB.
#     """
#     print(f"Processing file: {file_name}")
    
#     # Extract text from PDF
#     with pdfplumber.open(file_path) as pdf:
#         text = ''
#         for page in pdf.pages:
#             text += page.extract_text() or ''
    
#     if text:
#         # Summarize the text
#         summary = generate_summary_for_pdf_text(text)  # Corrected function call
        
#         # Extract keywords
#         keywords = extract_keywords_from_pdf_text(text)  # Corrected function call
        
#         # Store results in MongoDB
#         store_pdf_data(db, file_name, summary, keywords)
#         print(f"Successfully processed and stored {file_name}")
#     else:
#         print(f"No text extracted from {file_name}")

# def process_all_pdfs(pdf_links):
#     """
#     Download and process all PDFs from the provided dictionary of links.
#     """
#     for pdf_name, url in pdf_links.items():
#         file_path = download_pdf(pdf_name, url)
#         if file_path:
#             process_pdf(pdf_name, file_path)

# if __name__ == "__main__":
#     # Process all PDF links provided
#     process_all_pdfs(pdf_links)
#     print("All PDFs processed successfully!")
