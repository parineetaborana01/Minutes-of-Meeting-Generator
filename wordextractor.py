from docx import Document

def doc_text_extractor(file_path):
 file =Document(file_path)
 doc_text='sample_file.docx'
 for p in file.paragraphs:
  doc_text=doc_text+p.text+'\n'
 print(doc_text)    