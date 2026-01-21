from pypdf import PdfReader

def text_extractor(filepath):
    pdf_file=PdfReader(filepath)
    Content =''
    for page in pdf_file.pages:
        Content=Content+page.extract_text()+'\n'
    return Content         