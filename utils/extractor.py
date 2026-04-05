import pdfplumber
import docx2txt

def extract_text_from_file(file):
    """PDF and DOCX nundi text extract chestundi."""
    text = ""
    try:
        if file.name.endswith(".pdf"):
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
        elif file.name.endswith(".docx"):
            text = docx2txt.process(file)
        return text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
        
