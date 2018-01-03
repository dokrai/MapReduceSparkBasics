#!/usr/bin/python
#ELena Kaloyanova Popova

from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('AveragePrice')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile("GOOG.csv")

data = RDDvar.filter(lambda line: "Date" not in line)
stock = data.map(lambda line: (int((line.split(',')[0]).split('-')[0]),float(line.split(',')[4])))
number = data.map(lambda line: (int((line.split(',')[0]).split('-')[0]),1)) 

aggreg1 = stock.reduceByKey(lambda a,b: a+b)
aggreg2 = number.reduceByKey(lambda a,b: a+b)

union = aggreg1.join(aggreg2)

resultado = union.map(lambda line: (line[0], line[1][0]/line[1][1]))

resultado.saveAsTextFile("media.txt")