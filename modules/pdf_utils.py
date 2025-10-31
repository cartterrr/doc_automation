from PyPDF2 import PdfMerger, PdfReader

def merge_pdfs(list_of_paths, output_path):
    merger = PdfMerger()
    for p in list_of_paths:
        merger.append(p)
    with open(output_path, "wb") as f:
        merger.write(f)
    merger.close()

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    texts = []
    for page in reader.pages:
        t = page.extract_text()
        if t:
            texts.append(t)
    return "\n\n".join(texts)