import PyPDF2 
import textract
import requests
import os, sys
import time
from urllib.request import urlopen
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
# st='1530521847_HDFC3'
# file_url = "https://gullakh.s3-us-west-2.amazonaws.com/2/1530521847_HDFC3.pdf"
# ts = int(time.time())
# ts = str(ts)
# st=st+ts;
# response = urlopen(file_url)
# file = open(st, 'wb')
# file.write(response.read())
# file.close()
# print('Download Complete')

for i in range(1,39):
	st='ICICI'
	st+=str(i)
	st+='.pdf'
	pdfFileObj = open(st,'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	num_pages = pdfReader.numPages
	count = 0
	text = ""

	while count < num_pages:
	    pageObj = pdfReader.getPage(count)
	    count +=1
	    text += pageObj.extractText()

	if text == "":
		text = textract.process(st)
		print(str(i) + " OCR USED")
	else:
		print(str(i) + " OCR NOT USED")

	text = str(text)
	tokens = word_tokenize(text)
	detailed="DETAILED"
	statement="STATEMENT"
	checkdetailed=re.compile(detailed)
	checkstatement=re.compile(statement)

	if((checkstatement.search(tokens[1]) or checkstatement.search(tokens[3])) and (checkdetailed.search(tokens[0]) or checkdetailed.search(tokens[2]))):
		print("DETAILED STATEMENT") 
	else:
		print("NORMAL STATEMENT")
	print('\n')
	# import re
	# text = 'The quick brown\nfox jumps*over the lazy dog.'
	# print(re.split('; |, |\*|\n',text))
	# search = 'DETAILED'
	# if search in tokens:
	# 	print('Found')
	# else:
	# 	print('Not found')

	# os.remove(st)