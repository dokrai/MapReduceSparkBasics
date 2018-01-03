#!/usr/bin/python
# Elena Kaloyanova Popova

import sys
import re


#buscar = sys.argv[1]
#print(buscar)

for line in sys.stdin:
	line = re.sub( r'^\W+|\W+$', '', line ) # parsear linea
	words = re.split(r"\W+", line) # dividir linea en palabras

	for words in words: # mostrar palabras de la frase
		print( words.lower() + "\t1" )