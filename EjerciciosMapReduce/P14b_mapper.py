#!/usr/bin/python
#Elena Kaloyanova Popova
import sys
import re

#lists which contains the ids for every range of rates
ids_one = []
ids_two = []
ids_three = []
ids_four = []
ids_five = []

def clasify_rating(movie,rating):
	if float(rating) <= 1:
		ids_one.append(movie)
	elif float(rating) <= 2:
		ids_two.append(movie)
	elif float(rating) <= 3:
		ids_three.append(movie)
	elif float(rating) <= 4:
		ids_four.append(movie)
	elif float(rating) <= 5:
		ids_five.append(movie)

def show_list(list_id,rating):
	if len(list_id) > 0:
		for i in range(len(list_id)):
			print(str(rating) + "," + list_id[i])

def clasifier():
	for line in sys.stdin:
		line = re.sub( r'^\W+|\W+$', '', line )
		words = line.split(",", 2)
		clasify_rating(words[0],words[1])

def mapper():
	show_list(ids_five,5)
	show_list(ids_four,4)
	show_list(ids_three,3)
	show_list(ids_two,2)
	show_list(ids_one,1)

clasifier()
mapper()