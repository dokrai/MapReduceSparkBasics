#!/usr/bin/python
#ELena Kaloyanova Popova

from pyspark import SparkConf, SparkContext
import string
import sys

def users_average(RDDrating):
	ratingsData = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[0]),float(line.split(',')[2])))
	numRatings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[0]),1))
	aggreg1 = ratingsData.reduceByKey(lambda a,b: a+b)
	aggreg2 = numRatings.reduceByKey(lambda a,b: a+b)
	union = aggreg1.join(aggreg2)
	avg = union.map(lambda line: (line[0], line[1][0]/line[1][1]))
	avg.saveAsTextFile("users.txt")

def overall_average(RDDrating):
	ratings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (1,float(line.split(',')[2])))
	aggreg1 = ratings.reduceByKey(lambda a,b: a+b)
	result = aggreg1.map(lambda line: (line[1]/423)) #423 son los que tengo en el fichero de prueba
	result.saveAsTextFile("overall.txt")

def movies_average(RDDrating,RDDmovies): #tildes...
	#moviesData = RDDmovies.filter(lambda line: "movieId" not in line).map(lambda line: (int(line.split(',')[0]),str(line.split(',')[1])))
	ratingsData = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),float(line.split(',')[2])))
	numRatings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),1))
	aggreg1 = ratingsData.reduceByKey(lambda a,b: a+b)
	aggreg2 = numRatings.reduceByKey(lambda a,b: a+b)
	union = aggreg1.join(aggreg2)
	avg = union.map(lambda line: (line[0], line[1][0]/line[1][1]))
	#result = moviesData.join(avg)
	avg.saveAsTextFile("movies.txt")

def genres_average(RDDrating,RDDmovies): #ni idea...
	
	avg.saveAsTextFile("genres.txt")

def top10(RDDrating,RDDmovies,sc): #tildes...
	#moviesData = RDDmovies.filter(lambda line: "movieId" not in line).map(lambda line: (int(line.split(',')[0]),str(line.split(',')[1])))
	ratingsData = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),float(line.split(',')[2])))
	numRatings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),1))
	aggreg1 = ratingsData.reduceByKey(lambda a,b: a+b)
	aggreg2 = numRatings.reduceByKey(lambda a,b: a+b)
	union = aggreg1.join(aggreg2)
	avg = union.map(lambda line: (line[1][0]/line[1][1], line[0]))
	#result = moviesData.join(avg)
	ordered = avg.sortByKey(False)
	ten = ordered.take(10)
	top = sc.parallelize(ten,1)
	top.saveAsTextFile("top10.txt")

def top10_month(RDDrating,RDDmovies): #no entiendo lo que pide...
	print("Top 10 each month")

def main():
	conf = SparkConf().setMaster('local').setAppName('MovieRatings')
	sc = SparkContext(conf = conf)

	RDDrating = sc.textFile("notas.csv")
	RDDmovies = sc.textFile("movies.csv")

	ar = sys.argv[1]
	op = int(ar)

	if op == 1:
		users_average(RDDrating)
	elif op == 2:
		overall_average(RDDrating)
	elif op == 3:
		movies_average(RDDrating,RDDmovies)
	elif op == 4:
		genres_average(RDDrating,RDDmovies)
	elif op == 5:
		top10(RDDrating,RDDmovies,sc)
	elif op == 6:
		top10_month(RDDrating,RDDmovies)
	else:
		raise ValueError("WRONG OPTION")

main()