

from dataclasses import dataclass
from pypdf import PdfReader
import os

from sympy import fibonacci

@dataclass
class PDFService:
    file_path: str
    
    def retrieve_text_from_pdf(self):
        pdf_reader = PdfReader(file_path)
        pages = pdf_reader.pages
        full_text = ''
        for page in pages:
            full_text+=page.extract_text()     
        
        with open(os.path.join(os.getcwd(),'test.txt'), 'w') as file: 
            file.write(full_text)
   
if __name__ == "__main__":
    file_name = 'harry_potter_1.pdf'
    file_path = f'''{os.path.join(os.getcwd(),file_name)} '''
    PDFService(file_path=file_path).retrieve_text_from_pdf()