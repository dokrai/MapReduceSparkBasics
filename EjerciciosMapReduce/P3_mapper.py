#!/usr/bin/python
# Elena Kaloyanova Popova

import sys
import re


"""
This program searchs for the average mass per year for the type of meteorites "H6".
"""
wanted = "H6"
count = 0

def parse_type(met_type,mass):
	if(mass != ""):
		if mass[0] == " ":
			return (met_type+mass),False
		else:
			return met_type,True
	else:
		return "ERROR", False

def parse_year(landing):
	if landing != "":
		date = landing.split(" ",3)
		year = (date[0].split("/",3))[2]
		return year
	else:
		return "0000"

for line in sys.stdin:
	if count > 0:
		line = re.sub( r'^\W+|\W+$', '', line )
		words = line.split(',', 10)
		if len(words) > 6:
			met_type, simple = parse_type(words[3],words[4])
			if met_type == wanted:
				if simple is True:
					mass = words[4]
					year = parse_year(words[6])
				else:
					mass = words[5]
					year = parse_year(words[7])
				print(year + "\t" + mass) # get the movie_id and the raiting 
	else:
		count = count + 1