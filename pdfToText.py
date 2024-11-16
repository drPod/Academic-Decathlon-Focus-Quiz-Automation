import PyPDF2


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file."""
    text = []
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text.append(page.extract_text())
    return "\n".join(text)
