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
	avg = union.map(lambda line: (line[0], round(line[1][0]/line[1][1],2)))
	avg.saveAsTextFile("users.txt")

def overall_average(RDDrating):
	ratings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (1,float(line.split(',')[2])))
	aggreg1 = ratings.reduceByKey(lambda a,b: a+b)
	numRatings = ratings.count()
	result = aggreg1.map(lambda line: (round(line[1]/numRatings,2))) 
	result.saveAsTextFile("overall.txt")

def movies_average(RDDrating,RDDmovies): 
	moviesData = RDDmovies.filter(lambda line: "movieId" not in line).map(lambda line: (int(line.split(',')[0]),line.split(',')[1]))
	ratingsData = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),float(line.split(',')[2])))
	numRatings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),1))
	aggreg1 = ratingsData.reduceByKey(lambda a,b: a+b)
	aggreg2 = numRatings.reduceByKey(lambda a,b: a+b)
	union = aggreg1.join(aggreg2)
	avg = union.map(lambda line: (line[0], round(line[1][0]/line[1][1],2)))
	union2 = moviesData.join(avg)
	result = union2.map(lambda line: (line[1][0], line[1][1]))
	result.saveAsTextFile("movies.txt")

def genres_average(RDDrating,RDDmovies): 
	moviesData1 = RDDmovies.filter(lambda line: "movieId" not in line).filter(lambda line: len(line.split(','))==3).map(lambda line: (int(line.split(',')[0]), str(line.split(',')[2])))
	moviesData2 = RDDmovies.filter(lambda line: "movieId" not in line).filter(lambda line: len(line.split(','))==4).map(lambda line: (int(line.split(',')[0]), str(line.split(',')[3])))
	moviesData3 = RDDmovies.filter(lambda line: "movieId" not in line).filter(lambda line: len(line.split(','))==5).map(lambda line: (int(line.split(',')[0]), str(line.split(',')[4])))
	moviesDataAux = moviesData1.union(moviesData2)
	moviesData = moviesDataAux.union(moviesData3)
	ratingsData = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),float(line.split(',')[2])))
	numRatings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),1))
	aggreg1 = ratingsData.reduceByKey(lambda a,b: a+b)
	aggreg2 = numRatings.reduceByKey(lambda a,b: a+b)
	union = aggreg1.join(aggreg2)
	avg = union.map(lambda line: (line[0], line[1][0]/line[1][1]))
	union2 = moviesData.join(avg)

	movies_avg = union2.map(lambda line: (line[1][0], line[1][1]))
	moviesPerGenre = union2.map(lambda line: (line[1][0], 1))
	aggreg3 = movies_avg.reduceByKey(lambda a,b: a+b)
	aggreg4 = moviesPerGenre.reduceByKey(lambda a,b: a+b)
	union3 = aggreg3.join(aggreg4)
	result = union3.map(lambda line: (line[0], line[1][0]/line[1][1]))
	result.saveAsTextFile("genres.txt")

def top10(RDDrating,RDDmovies,sc): 
	moviesData = RDDmovies.filter(lambda line: "movieId" not in line).map(lambda line: (int(line.split(',')[0]),line.split(',')[1]))
	ratingsData = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),float(line.split(',')[2])))
	numRatings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]),1))
	aggreg1 = ratingsData.reduceByKey(lambda a,b: a+b)
	aggreg2 = numRatings.reduceByKey(lambda a,b: a+b)
	union = aggreg1.join(aggreg2)
	avg = union.map(lambda line: (line[1][0]/line[1][1], line[0]))
	ordered = avg.sortByKey(False)
	ten = ordered.take(10)
	top = sc.parallelize(ten,1)
	topMovies = top.map(lambda line: (line[1], line[0])).join(moviesData)
	result = topMovies.map(lambda line: (line[1][1]))
	result.saveAsTextFile("top10.txt")

def main():
	#Spark configuration
	conf = SparkConf().setMaster('local').setAppName('MovieRatings')
	sc = SparkContext(conf = conf)

	RDDrating = sc.textFile("ratings.csv")
	RDDmovies = sc.textFile("movies.csv")

	ar = sys.argv[1] # the user choose the question
	op = int(ar)

	if op == 1:
		users_average(RDDrating) # average rating given by each user
	elif op == 2:
		overall_average(RDDrating) # overall average raiting
	elif op == 3:
		movies_average(RDDrating,RDDmovies) # average rating of each movie
	elif op == 4:
		genres_average(RDDrating,RDDmovies) # average rating of each genre
	elif op == 5:
		top10(RDDrating,RDDmovies,sc) # top10
	else:
		raise ValueError("WRONG OPTION")

main()