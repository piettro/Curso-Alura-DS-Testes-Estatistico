import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.stats.weightstats import zconfint
from statsmodels.stats.weightstats import DescrStatsW

data_movies_imdb = pd.read_csv('Data/tmdb_5000_movies.csv')
print(data_movies_imdb.describe())

ratings = pd.read_csv('Data/ratings.csv')
print(ratings.describe())

vote_avg_from_movies_with_more_than_ten_vote = data_movies_imdb.query('vote_count >= 10')['vote_average']

np.random.seed(75243)
temp = vote_avg_from_movies_with_more_than_ten_vote.sample(frac=1)

means = list()
means = [temp[0:i].mean() for i in range(1, len(temp))]

plt.plot(means)
plt.show()

min_interval, max_interval = zconfint(vote_avg_from_movies_with_more_than_ten_vote)
print(f'In Z conf the min interval to average is {min_interval} and the max interval is {max_interval}')

descr_all_with_ten_votes = DescrStatsW(vote_avg_from_movies_with_more_than_ten_vote)
min_interval, max_interval = descr_all_with_ten_votes.tconfint_mean()
print(f'In T conf the min interval to average is {min_interval} and the max interval is {max_interval}')