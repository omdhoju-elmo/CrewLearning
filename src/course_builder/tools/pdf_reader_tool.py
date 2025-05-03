from crewai.tools import tool
import fitz  # PyMuPDF

@tool("extract_pdf_content")
def extract_pdf_content(pdf_file_path: str) -> str:
    """Reads a PDF from the local file system and returns all text"""
    text = ""
    with fitz.open(pdf_file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text
