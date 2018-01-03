#!/usr/bin/python
#ELena Kaloyanova Popova

from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('Shakespeare')
sc = SparkContext(conf = conf)

RDDtext = sc.textFile("shakespeare.txt")

sentences = RDDtext.flatMap(lambda line: line.split())

words = sentences.map(lambda word: (str(word.lower()).translate(None,string.punctuation)))

words.saveAsTextFile("phrases.txt")