from datetime import date
from os import listdir

import matplotlib.pyplot as pyplot
import numpy

from model import Movie


def parse_movie(movie_string, year):
    if year <= 2016:
        return Movie(movie_string)
    elif year == 2017:
        parsed_values = movie_string.lstrip(
            '1234567890. \u200e').rsplit(' - ', 1)
        month_and_day = list(map(int, parsed_values[1].split('/')))
        watch_date = date(year, month_and_day[0], month_and_day[1])
        return Movie(parsed_values[0], watch_date)
    elif year >= 2018:
        parsed_values = movie_string.lstrip(
            '1234567890. \u200e').rsplit(' - ', 2)
        month_and_day = list(map(int, parsed_values[1].split('/')))
        watch_date = date(year, month_and_day[0], month_and_day[1])
        return Movie(parsed_values[0], watch_date, parsed_values[2])


# get years
years = [int(year.rstrip('.tx')) for year in listdir('data')]
years.sort()

movie_data = {}
# for year in years:
#     total = 0
#     with open('data/{0}.txt'.format(year)) as file:
#         for line in file:
#             total += 1
#             movie = Movie.parse_movie(line, year)
#             print(movie)
#     movies_watched.append(total)

for year in years:
    movies_watched = []
    with open('data/{0}.txt'.format(year)) as file:
        for line in file:
            movies_watched.append(parse_movie(line.strip(), year))
    
    movie_data[year] = movies_watched

# pyplot.bar(years, movies_watched, width=.6)
# pyplot.title("Movies Watched")
# pyplot.show()

for k, v in movie_data.items():
    print(k)
    for movie in v:
        print(movie)