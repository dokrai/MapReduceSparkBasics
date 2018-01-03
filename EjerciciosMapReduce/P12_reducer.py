#!/usr/bin/python
# Elena Kaloyanova Popova

import sys

previous = None
suma = 0

for line in sys.stdin:
	key, value = line.split('\t')
	if key != previous:
		if previous is not None:
			print("El dominio " + previous + " aparece " + str(suma) + " veces.")
		previous = key
		suma = 0
	suma = suma + int(value)
print("El dominio " + previous + " aparece " + str(suma) + " veces.")