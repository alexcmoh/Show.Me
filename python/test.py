# Testing python function call

import pandas as pd
import numpy as np
import random
from random import randint

# Returns a list of n entries
# Each entry is [movie title, genres, average rating]
# This is also what the script will need to receive later
def getTitle(n):

	df = pd.read_csv("data.copy.subset.tsv", sep='\t')
	df_titles = df["primaryTitle"]
	df_ratings = df["averageRating"]
	df_votes = df["numVotes"]
	df_genres = df["genres"]

	# Get n random titles
	titles = list()
	r = random.sample(range(0, len(df)), n)
	for i in r:
		title = df["primaryTitle"].iloc[i]
		genres = df["genres"].iloc[i]
		averageRating = df["averageRating"].iloc[i]
		titles.append([title, genres, averageRating])

	return titles

# print(getTitle(1))

def intersection(str1, str2):
	diff = list(set(str1) & set(str2))
	return(len(diff))

def kNearest(title, genres, rating, threshold):
	test = [title, genres, rating]
	# print("Test instance:", title, genres, rating)
	
	# Read training data
	df = pd.read_csv("data.copy.subset.tsv", sep='\t')
	
	# Get relevant information
	df_titles = df["primaryTitle"]
	df_ratings = df["averageRating"]
	df_votes = df["numVotes"]
	df_genres = df["genres"]

	dists = list()
	recs = list()
	
	for i in range(len(df_titles)):

		titleList = str.split(df_titles.iloc[i], " ")
		d1 = len(str.split(title, " "))+len(titleList)-intersection(title, titleList)
		# print("# same words in title:", d1)
		
		genreList = str.split(df_genres.iloc[i], ",")
		d2 = len(genres)+len(genreList)-intersection(genres, genreList)
		# print("# same words in genre:", d2)

		score = (0.21*d1 + 0.93*d2) 
		if title == df_titles.iloc[i]:
			score = 0.0

		# print(score)
		if score != 0:
			dists.append(score)
			if score < threshold:
				recs.append(df.iloc[i])

	if (len(recs) < 2):
		# print("\tRestarting with threshold", threshold+0.5)
		ret = kNearest(title, genres, rating, threshold+0.5)
		return ret
	
	# print("Total number of recommendations:", len(recs))

	# print("Mean distance:", sum(dists)/len(dists))
	# print("Min distance:", min(dists))
	# print("Max distance:", max(dists))

	# print(title, len(recs)) # gets to here correctly, then goes to 3.1.2
	return recs

def test():

	df = pd.read_csv("data.copy.subset.tsv", sep='\t')
	df_titles = df["primaryTitle"]
	df_ratings = df["averageRating"] # doesn't end up getting used either, but good to have
	df_votes = df["numVotes"] # doesn't end up getting used, i think
	df_genres = df["genres"]

	for i in range(len(df_titles)):
		print(df_titles.iloc[i], "@", df_genres.iloc[i], "@", df_ratings.iloc[i], "\n", end=" ")

	result = list()

	# Use N random instances as test set
	r = random.sample(range(0, len(df)), 10)
	print("\nYou liked:")
	for i in r:
		title = df["primaryTitle"].iloc[i]
		genres = df["genres"].iloc[i]
		averageRating = df["averageRating"].iloc[i]
		print("\t", title)
		result += kNearest(title, genres, averageRating, 0.3)

	print("\nTotal number of recommendations:", len(result))

	n = 10
	if (len(result) < 10):
		n = len(result)

	print("\nRandom sample of n recommendations:")
	sample = random.sample(result, n)
	for data in sample:
		print("\t", data["primaryTitle"])

test()





