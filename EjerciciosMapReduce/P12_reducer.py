#!/usr/bin/python
# Elena Kaloyanova Popova

import sys

previous = None
total = 0

for line in sys.stdin:
	key, value = line.split('\t')
	if key != previous: # we keep adding until we find the next domain
		if previous is not None:
			print("Domain " + previous + " appears " + str(total) + " times.")
		previous = key
		total = 0
	total = total + int(value)
print("Domain " + previous + " appears " + str(total) + " times.")