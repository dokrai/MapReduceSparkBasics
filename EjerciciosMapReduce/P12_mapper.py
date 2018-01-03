#!/usr/bin/python
# Elena Kaloyanova Popova

import sys
import re

dominio = False

for line in sys.stdin:
	line = re.sub( r'^\W+|\W+$', '', line ) # parsear linea
	words = re.split(r"\W+", line) # dividir linea en palabras

	for words in words: # mostrar palabras de la frase
		if dominio == True:
			print(words.lower() + "\t1")
			dominio = False
		if words =="GET" or words == "POST":
			dominio = True