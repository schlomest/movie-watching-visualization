import numpy

def get_yearly_totals(movie_data):
    """y data for movies watched per year bar chart"""
    return [len(movie_data[k]) for k in movie_data.keys()]


def get_weekday_totals(movie_data):
    """data for movies watched by weekday bar chart"""
    movies_by_weekday = {"Sunday": 0, "Monday": 0, "Tuesday": 0,
                         "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0}
    for year in movie_data.keys():
        if year >= 2017:
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

    return movies_by_weekday

def get_monthly_totals(movie_data):
    """data for movies watched per month graph"""
    movie_list = []
    for k, v in movie_data.items():
        if k >= 2017:
            movie_list += v

    monthly_data = {}
    for movie in movie_list:
        coverted_datetime = numpy.datetime64(movie.date_watched.isoformat()[:-3])
        if coverted_datetime in monthly_data.keys():
            monthly_data[coverted_datetime] += 1
        else:
            monthly_data[coverted_datetime] = 1   
    
    return monthly_data


def get_ratings_totals(movie_data):
    """data for movies ratings pie chart"""
    ratings = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for year in movie_data.keys():
        if year >= 2018:
            for movie in movie_data[year]:
                if movie.rating:
                    ratings[movie.rating] += 1

    return ratings
