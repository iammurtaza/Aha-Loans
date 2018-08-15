#!bin/bash

for i in {1..38}
do
	var="ICICI"
	var2=".pdf"
	c=$var$i$var2
	pdftotext -f 1 -l 1 $c - | grep -q 'DETAILED STATEMENT'

	# if pdftotext -f 1 -l 1 $c - | grep -q 'DETAILED STATEMENT'; then
	# 	echo $res
	# else
	# 	echo $res2
	# fi

	if [ $? -eq 0 ]; then
		echo "$i DETAILED"
	else
		echo "$i NORMAL"
	fi
done