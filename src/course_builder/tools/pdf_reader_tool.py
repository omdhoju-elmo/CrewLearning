from crewai.tools import tool
import fitz  # PyMuPDF

@tool("extract_pdf_content")
def extract_pdf_content() -> str:
    """Reads a PDF from the local file system and returns all text"""
    file_path = "src/course_builder/data/travel.pdf"  # Update path as needed
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text
