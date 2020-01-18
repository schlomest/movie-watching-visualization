from datetime import date
from os import listdir

import matplotlib.pyplot as pyplot
import numpy

from model import Movie


def parse_movie(movie_string, year):
    """parse movie data according to each year's data format"""
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


def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, -20),
                    textcoords="offset points",
                    ha='center', va='bottom')


# get years
years = [int(year.rstrip('.tx')) for year in listdir('data')]
years.sort()

# create dictionary of movie data
# key: year watched
# value: list of movies watched that year
movie_data = {}
for year in years:
    movies_watched = []
    with open('data/{0}.txt'.format(year)) as file:
        for line in file:
            movies_watched.append(parse_movie(line.strip(), year))

    movie_data[year] = movies_watched

# Bar graph displaying number of movies watched per year
totals = [len(movie_data[k]) for k in movie_data.keys()]

fig, ax = pyplot.subplots()
rects = ax.bar(movie_data.keys(), totals, width=.6)
ax.set_title('Total Movies Watched')
autolabel(rects, ax)
fig.tight_layout()
pyplot.show()

# movies I loved
print("\nMovies I loved")
print("--------------")
for movie_list in movie_data.values():
    for movie in movie_list:
        if movie.rating == 5:
            print(movie)

# bar char for days of the week
movies_by_weekday = {"Sunday": 0, "Monday": 0, "Tuesday": 0,
                     "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0}
for year in movie_data.keys():
    if year > 2016:
        for movie in movie_data[year]:
            if movie.date_watched.weekday() == 6:
                movies_by_weekday["Sunday"] += 1
            elif movie.date_watched.weekday() == 0:
                movies_by_weekday["Monday"] += 1
            elif movie.date_watched.weekday() == 1:
                movies_by_weekday["Tuesday"] += 1
            elif movie.date_watched.weekday() == 2:
                movies_by_weekday["Wednesday"] += 1
            elif movie.date_watched.weekday() == 3:
                movies_by_weekday["Thursday"] += 1
            elif movie.date_watched.weekday() == 4:
                movies_by_weekday["Friday"] += 1
            elif movie.date_watched.weekday() == 5:
                movies_by_weekday["Saturday"] += 1

fig, ax = pyplot.subplots()
rects = ax.bar(movies_by_weekday.keys(), movies_by_weekday.values(), width=.6)
ax.set_title('Movies Watched by Weekday')
autolabel(rects, ax)
fig.tight_layout()
pyplot.show()