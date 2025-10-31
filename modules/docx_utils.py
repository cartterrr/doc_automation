from docx import Document

def extract_text_from_docx(path):
    doc = Document(path)
    full = []
    for para in doc.paragraphs:
        full.append(para.text)
    return "\n".join(full)