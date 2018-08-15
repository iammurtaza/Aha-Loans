import pdftotext
import requests
import sys
import os
import time
import re
import string
from urllib.request import urlopen
from nltk.tokenize import word_tokenize

def main():
	# file_url=sys.argv[1]
	# bank_type=sys.argv[2]

	# if(bank_type == "icici"):
	# 	name = file_url.split('/')
	# 	name2 = name[-1].split('.')
	# 	filename = name2[0]
	# 	ts = int(time.time())
	# 	ts = str(ts)
	# 	filename=filename+'_'+ts+'.pdf';
	# 	response = urlopen(file_url)
	# 	file = open(filename, 'wb')
	# 	file.write(response.read())
	# 	file.close()
	# 	print(checkicici(filename))
	# 	os.remove(filename)

	# else:
	# 	print("NOT ICICI")
	for i in range(1,39):
		filename = "ICICI"+str(i)+".pdf"
		print(str(i) + " " + checkicici(filename))

def checkicici(filename):
	with open(filename, "rb") as f:
		pdf = pdftotext.PDF(f)
	
	text = str(pdf[0])
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

# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/2/1530521847_HDFC3.pdf hdfc
# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/2/1530598673_ICICI6.pdf icici
# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/php5Dt9Xf.pdf axis
# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/2/1530277413_ICICI%20Stmt.pdf icici
# python3 -W ignore detailcheck.py https://gullakh.s3-us-west-2.amazonaws.com/Statement_JAN2018_343497535.pdf icici