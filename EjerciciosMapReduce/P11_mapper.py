#!/usr/bin/python
#Elena Kaloyanova Popova

import sys
import re

"""
This program searchs for a given pattern, in this case "must not".
"""
count = 1
for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    if(line.find('must not') >= 0): # look if the line contains the pattern, if so prints the number of the line
    	print(str(count))
    count = count+1;
