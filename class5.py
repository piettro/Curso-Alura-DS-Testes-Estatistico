import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.stats.weightstats import zconfint
from statsmodels.stats.weightstats import ztest 
from scipy.stats import ttest_ind
from statsmodels.stats.weightstats import DescrStatsW

movies = pd.read_csv('Data/movies.csv')
ratings = pd.read_csv('Data/ratings.csv')
ratings_movie_1 = ratings.query('movieId == 1')

descr_ratings = DescrStatsW(ratings.rating)
descr_ratings_movie_1 = DescrStatsW(ratings_movie_1.rating)
compare = descr_ratings.get_compare(descr_ratings_movie_1)

print(compare.summary())

plt.boxplot([ratings.rating, ratings_movie_1.rating], labels=["All Ratings", "Toy Story"])
plt.title("Distributions of ratings per movie")
plt.show()

descr_ratings = DescrStatsW(ratings.rating)
descr_ratings_movie_1 = DescrStatsW(ratings_movie_1[3:12].rating)
compare = descr_ratings.get_compare(descr_ratings_movie_1)

print(compare.summary(use_t=True))

plt.boxplot([ratings.rating, ratings_movie_1[3:12].rating], labels=["All Ratings", "Toy Story (3 to 12)"])
plt.title("Distributions of ratings per movie")
plt.show()