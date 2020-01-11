from os import listdir
from typing import List

import matplotlib.pyplot as pyplot
import numpy

# class Movie():
#     def __init__(self, name, date_watched=None, rating=None):
#         self.name = name
#         self.date_watched = date_watched
#         self.rating = rating

#     def __repr__(self):
#         return self.name

# MovieList = List[Movie]

# movie_list = []

# with open('data/2015.txt') as file:
#     for line in file:
#         movie = Movie(line.strip())
#         movie_list.append(movie)


# get years
years = [int(year.rstrip('.tx')) for year in listdir('data')]
years.sort()

movies_watched = []
for year in years:
    total = 0
    with open('data/{0}.txt'.format(year)) as file:
        for line in file:
            total += 1
    movies_watched.append(total)


pyplot.bar(years, movies_watched, width=.6)
pyplot.title("Movies Watched")
pyplot.show()
