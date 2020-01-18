class Movie():
    def __init__(self, name, date_watched=None, rating=None):
        self.name = name
        self.date_watched = date_watched

        if rating == 'n/a':
            self.rating = None
        else:
            self.rating = rating

    def __repr__(self):
        return 'Movie(name={0}, date_watched={1}, rating={2})'.format(self.name, self.date_watched, self.rating)

    def __str__(self):
        return self.name
