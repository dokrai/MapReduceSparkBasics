#!/usr/bin/python
#ELena Kaloyanova Popova

from pyspark import SparkConf, SparkContext
import string
import sys

#Spark configuration
conf = SparkConf().setMaster('local').setAppName('MeteoriteLandings')
sc = SparkContext(conf = conf)

RDDlandings = sc.textFile("Meteorite_Landings.csv")
met_type = ","+sys.argv[1]+","

meteoritesData = RDDlandings.filter(lambda line: met_type in line)
landingsInfo = meteoritesData.map(lambda line: (line.split(",")[0],line.split(',')[4], line.split(',')[6].split(" ")[0]))
landingsCorrect = landingsInfo.filter(lambda line: ((line[1] is not u'') and (line[2] is not u'')))
landingsInfo2 = landingsCorrect.map(lambda line: (line[2].split("/")[2],float(line[1])))
landingsCount = landingsCorrect.map(lambda line: (line[2].split("/")[2],1))
massPerYear = landingsInfo2.reduceByKey(lambda a,b: a+b)
landingsPerYear = landingsCount.reduceByKey(lambda a,b: a+b)
union = massPerYear.join(landingsPerYear)

avgMass = union.map(lambda line: (int(line[0]), line[1][0]/line[1][1]))

avgMass.saveAsTextFile("landings.txt")