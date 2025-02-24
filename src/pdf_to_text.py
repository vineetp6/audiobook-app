import pymupdf  # Ensure it's imported correctly
import fitz  # Alias for PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text
