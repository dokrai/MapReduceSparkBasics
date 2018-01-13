#!/usr/bin/python
#Elena Kaloyanova Popova

import sys
import re
import csv

previous = None

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    rates = line.split(',', 2) 
    if rates[0] != previous:
        print("--------------------------")
        print("Movies in range " + rates[0] + ':')
        print("--------------------------")
        previous = rates[0]
    with open('movies.csv', encoding="utf8") as movies_csv: # search the movie in the movies list so we can get its title
        movies_data = csv.reader(movies_csv)
        for reg in movies_data:
            if(reg[0] == str(rates[1])):
                print(reg[1])
                break