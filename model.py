class Movie():
    def __init__(self, name, date_watched=None, rating=None):
        self.name = name
        self.date_watched = date_watched

        if rating == 'n/a' or rating == None:
            self.rating = None
        else:
            self.rating = int(rating)

    def __repr__(self):
        return 'Movie(name={}, date_watched={}, rating={})'.format(self.name, self.date_watched, self.rating)

    def __str__(self):
        return self.name
