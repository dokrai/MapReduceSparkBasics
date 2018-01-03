#!/usr/bin/python
# Elena Kaloyanova Popova

import sys
import re

linea = 0
ignorar = ""

for line in sys.stdin:
	if linea == 0:
		re.sub( r'^\W+|\W+$', '' , ignorar)
		linea = linea + 1
	else:
		line = re.sub( r'^\W+|\W+$', '', line ) # parsear linea	
		numbers = line.split(',', 4) # se trocea la línea para obtener los datos
		print(numbers[1] + "\t" + numbers[2])