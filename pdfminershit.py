from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import pdfminer

def main():
    filename="atm.pdf"
    # convert_pdf_to_txt(filename)
    extract_raw_text(filename)

def convert_pdf_to_txt(path):
    manager = PDFResourceManager() 
    codec = 'utf-8'
    caching = True
    output = io.BytesIO()
    converter = TextConverter(manager, output, codec=codec, laparams=LAParams())     

    interpreter = PDFPageInterpreter(manager, converter) 
    fp = open(path, 'rb')
    
    for page in PDFPage.get_pages(fp, [1-10],caching=caching, check_extractable=False):
        interpreter.process_page(page)

    convertedPDF = output.getvalue()  
    print(convertedPDF)
    fp.close(); 
    output.close()

def extract_raw_text(pdf_filename):
    output = io.StringIO()
    laparams = pdfminer.layout.LAParams() # Using the defaults seems to work fine

    with open(pdf_filename, "rb") as pdffile:
        pdfminer.high_level.extract_text_to_fp(pdffile, output, laparams=laparams)
    
    return output.getvalue()   

if __name__ == '__main__':
    main()