import os
import requests
import pdfplumber
from src.summarization import summarize_text
from src.keyword_extraction import extract_keywords
from src.db_operations import connect_to_mongo, store_pdf_data

# Directory for downloading PDFs
download_dir = 'downloaded_pdfs'

# Initialize MongoDB connection
db = connect_to_mongo()

def download_pdf(pdf_name, url):
    """
    Download PDF from a given URL and save it to the download directory.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(download_dir, f"{pdf_name}.pdf")
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"{pdf_name} downloaded successfully.")
            return file_path
        else:
            print(f"Failed to download {pdf_name}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading {pdf_name}: {e}")
        return None

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
        # Summarize the text
        summary = summarize_text(text, method="textrank")
        
        # Extract keywords
        keywords = extract_keywords(text, num_keywords=5)
        
        # Store results in MongoDB
        store_pdf_data(db, file_name, summary, keywords)
        print(f"Successfully processed and stored {file_name}")
    else:
        print(f"No text extracted from {file_name}")

def process_all_pdfs(pdf_links):
    """
    Download and process all PDFs from the provided dictionary of links.
    """
    for pdf_name, url in pdf_links.items():
        file_path = download_pdf(pdf_name, url)
        if file_path:
            process_pdf(pdf_name, file_path)

if __name__ == "__main__":
    # Process all PDF links provided
    process_all_pdfs(pdf_links)
    print("All PDFs processed successfully!")
