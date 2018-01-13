#!/usr/bin/python
# Elena Kaloyanova Popova

import sys
import re

domain = False

for line in sys.stdin:
	line = re.sub( r'^\W+|\W+$', '', line ) 
	words = re.split(r"\W+", line) 

	for words in words: # parse each line
		if domain == True:
			print(words.lower() + "\t1")
			domain = False
		if words =="GET" or words == "POST": #the next word after each GET or POST is the name of the domain
			domain = True