#!/usr/bin/python
# Elena Kaloyanova Popova

import sys

previous = None
total = 0
elements = 0

for line in sys.stdin:
	key, value = line.split('\t')
	if key != previous:
		if previous is not None:
			average = total/elements
			average = round(average,2)
			elements = 0
			print("The average for " + previous + " is " + str(average))
		previous = key
		total = 0
	total = total + float(value)
	elements = elements + 1
average = total/elements
average = round(average,2)
print("The average for " + previous + " is " + str(average))