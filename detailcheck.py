import PyPDF2 
import textract
import requests
import os
import sys
import time
import string
import re
from urllib.request import urlopen
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def main():
	file_url=sys.argv[1]
	bank_type=sys.argv[2]

	name = file_url.split('/')
	name2 = name[-1].split('.')
	st = name2[0]
	ts = int(time.time())
	ts = str(ts)
	st=st+'_'+ts+'.pdf';
	response = urlopen(file_url)
	file = open(st, 'wb')
	file.write(response.read())
	file.close()

	if(bank_type == "icici"):print(checkicici(st))
	else:print("NO")
	os.remove(st)

def checkicici(st):
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

	text = str(text)
	tokens = word_tokenize(text)
	detailed="DETAILED"
	statement="STATEMENT"
	checkdetailed=re.compile(detailed)
	checkstatement=re.compile(statement)

	if((checkdetailed.search(tokens[0]) and checkstatement.search(tokens[1])) or (checkdetailed.search(tokens[2]) or checkstatement.search(tokens[3]))):
		return("TRUE") 
	else:
		return("FALSE")

if __name__ == '__main__':
	main()

# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/2/1530521847_HDFC3.pdf icici
# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/2/1530598673_ICICI6.pdf icici