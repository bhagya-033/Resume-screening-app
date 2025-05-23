import PyPDF2

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text
