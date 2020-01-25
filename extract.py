from datetime import date
from os import listdir

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


def load_movie_data():
    """create movie data dictionary"""
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
    
    return movie_data
