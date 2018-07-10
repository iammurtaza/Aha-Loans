import PyPDF2
import requests
import sys
import os
import time
from PyPDF2 import PdfFileWriter, PdfFileReader
from urllib.request import urlopen

def main():
	# file_url=sys.argv[1]
	# password=sys.argv[2]
	# name = file_url.split('/')
	# name2 = name[-1].split('.')
	# filename = name2[0]
	# ts = int(time.time())
	# ts = str(ts)
	# filename=filename+'_'+ts+'.pdf';
	# response = urlopen(file_url)
	# file = open(filename, 'wb')
	# file.write(response.read())
	# file.close()
	
	filename = "Axis-Bank-protected.pdf"
	password = "gullakh@123"

	decrypt(filename, password)
	# os.remove(filename)
	os.remove("temp.pdf")

def decrypt(filename, password):
	
	pdfFileObj = open(filename,'rb')
	pdfFile = PdfFileReader(pdfFileObj)

	if pdfFile.isEncrypted:
		try:
			pdfFile.decrypt(password)
			print('File Decrypted (PyPDF2)')
		except:
			command="cp "+ filename +" temp.pdf; qpdf --password='" + password + "' --decrypt temp.pdf "+ filename
			os.system(command)
			print('File Decrypted (qpdf)')
			pdfFileObj = open(filename,'rb')
			pdfFile = PdfFileReader(pdfFileObj)
	else:
		print('File Not Encrypted')
	
	# num_pages = pdfFile.numPages
	# count = 0
	# text = ""
	# while count < num_pages:
	#     pageObj = pdfFile.getPage(count)
	#     count +=1
	#     text += pageObj.extractText()

	# text = str(text)
	# print(text)

if __name__ == '__main__':
	main()

# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/2/1530521847_HDFC3.pdf hdfc
# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/2/1530598673_ICICI6.pdf icici
# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/php5Dt9Xf.pdf axis
# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/2/1530277413_ICICI%20Stmt.pdf icici
# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/Statement_JAN2018_343497535.pdf icici