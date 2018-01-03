#!/usr/bin/python
#ELena Kaloyanova Popova

from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('MovieRatings')
sc = SparkContext(conf = conf)

RDDrating = sc.textFile("notas.csv")
RDDmovies = sc.textFile("movies.csv")

moviesData = RDDmovies.filter(lambda line: "movieId" not in line).map(lambda line: (int(line.split(',')[0]),str(line.split(',')[1])))
ratingsData = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),float(line.split(',')[2])))
numRatings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),1))

aggreg1 = ratingsData.reduceByKey(lambda a,b: a+b)
aggreg2 = numRatings.reduceByKey(lambda a,b: a+b)

union = aggreg1.join(aggreg2)

avg = union.map(lambda line: (line[0], line[1][0]/line[1][1]))

result = moviesData.join(avg)

result.saveAsTextFile("ratings.txt")