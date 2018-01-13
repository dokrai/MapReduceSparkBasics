#!/usr/bin/python
#Elena Kaloyanova Popova

from pyspark import SparkConf, SparkContext
import string
import sys

class Counter(object):

	count = 0

	def counter_up(self):
		self.count = self.count + 1
		return self.count

#Spark configuration
conf = SparkConf().setMaster('local').setAppName('GrepTool')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile("input.txt")
wanted = "must" # the pattern we will search in this case is "must"
num_line = Counter()

lines = RDDvar.map(lambda line: (str(line),num_line.counter_up()))
good_lines = lines.filter(lambda line: wanted in line[0])

good_lines.saveAsTextFile("output.txt")