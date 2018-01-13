#!/usr/bin/python
# Elena Kaloyanova Popova

import sys
import re

count = 0

for line in sys.stdin:
	if count > 0:
		line = re.sub( r'^\W+|\W+$', '', line )
		numbers = line.split(',', 4) 
		print(numbers[1] + "\t" + numbers[2]) # get the movie_id and the raiting 
	else:
		count = count + 1