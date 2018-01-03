#!/usr/bin/python
# Elena Kaloyanova Popova

import sys

previous = None
suma = 0
encontrada = False

#buscar = input().lstrip("0")
buscar = sys.argv[1]

for line in sys.stdin:
	key, value = line.split('\t')
	if key != previous:
		if previous == buscar:
			print("Hay " + str(suma)+ " palabras: " +previous)
			encontrada = True
		previous = key
		suma = 0
	suma = suma + int(value)
print("Ha acabado la búsqueda")
if encontrada == False:
	print("La palabra no estaba en el archivo")	
