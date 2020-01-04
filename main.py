from typing import List

class Movie():
    def __init__(self, name, date_watched=None, rating=None):
        self.name = name
        self.date_watched = date_watched
        self.rating = rating

    def __repr__(self):
        return self.name

MovieList = List[Movie]

movie_list = []

with open('data/2015.txt') as file:
    for line in file:
        movie = Movie(line.strip())
        print(movie)
        movie_list.append(movie)

print(movie_list)