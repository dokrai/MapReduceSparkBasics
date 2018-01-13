#!/usr/bin/python
# Elena Kaloyanova Popova

import sys

previous = None
total = 0
elements = 0

for line in sys.stdin:
	key, value = line.split('\t')
	if key != previous:
		if previous is not None: # we only calculate the avg once we are done with all the rates for the movie
			average = total/elements
			average = round(average,2)
			elements = 0
			print(previous + "," + str(average))
		previous = key
		total = 0
	total = total + float(value)
	elements = elements + 1
average = total/elements
average = round(average,2)
print(previous + "," + str(average))