import matplotlib.dates as mdates
import matplotlib.pyplot as pyplot
import numpy

from extract import load_movie_data
from transform import get_ratings_totals, get_weekday_totals, get_yearly_totals


def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, -20),
                    textcoords="offset points",
                    ha='center', va='bottom')


movie_data = load_movie_data()

# MOVIES WATCHED PER YEAR BAR CHART
totals = get_yearly_totals(movie_data)
fig, ax = pyplot.subplots()
rects = ax.bar(movie_data.keys(), totals, width=.6)
ax.set_title('Total Movies Watched')
autolabel(rects, ax)
fig.tight_layout()
pyplot.show()

# MOVIES WATCHED PER DAY OF THE WEEK BAR CHART
movies_by_weekday = get_weekday_totals(movie_data)
fig, ax = pyplot.subplots()
rects = ax.bar(movies_by_weekday.keys(),
               movies_by_weekday.values(), width=.6, color='g')
ax.set_title('Movies Watched by Weekday')
autolabel(rects, ax)
fig.tight_layout()
pyplot.show()


# RATINGS PIE CHART
ratings = get_ratings_totals(movie_data)
# Currently there are 0 'hated' ratings, so I removed that data from the vizualization
labels = "Didn't Like", 'Meh', 'Liked', 'Loved'
sizes = list(ratings.values())[1:]

fig1, ax1 = pyplot.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=180)
ax1.axis('equal')
pyplot.show()


# movies I loved
print("\nMovies I loved")
print("--------------")
for movie_list in movie_data.values():
    for movie in movie_list:
        if movie.rating == 5:
            print(movie)
print("--------------")
