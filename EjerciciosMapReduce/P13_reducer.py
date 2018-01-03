#!/usr/bin/python
# Elena Kaloyanova Popova

import sys

previous = None
suma = 0
elementos = 0

for line in sys.stdin:
	key, value = line.split('\t')
	if key != previous:
		if previous is not None:
			media = suma/elementos
			elementos = 0
			print("La media para el año " + previous + " es " + str(media))
		previous = key
		suma = 0
	suma = suma + float(value)
	elementos = elementos + 1
print("La media para el año " + previous + " es " + str(media))