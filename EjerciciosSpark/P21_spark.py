#!/usr/bin/python
#ELena Kaloyanova Popova

from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('WordCount')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile("input.txt")
buscar = sys.argv[1]

words = RDDvar.flatMap(lambda line: line.split())

result = words.map(lambda word: (str(word.lower()).translate(None,string.punctuation),1))

aggreg1 = result.reduceByKey(lambda a, b: a+b)

numero = aggreg1.filter(lambda line: buscar in line)

numero.saveAsTextFile("output.txt")