#!/usr/bin/python
# Elena Kaloyanova Popova

import sys
import re

count = 0

for line in sys.stdin:
	if count > 0: # ignore the first line
		line = re.sub( r'^\W+|\W+$', '', line ) 
		words = line.split(',', 7) 
		print(words[0][0:4] + "\t1" + words[4]) # we get the year and the price
	else:
		count = count + 1