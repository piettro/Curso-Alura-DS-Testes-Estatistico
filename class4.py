import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.stats.weightstats import zconfint
from statsmodels.stats.weightstats import ztest

movies = pd.read_csv('Data/movies.csv')
print(movies.describe())

ratings = pd.read_csv('Data/ratings.csv')
print(ratings.describe())

ratings_movie_1 = ratings.query('movieId == 1')
print(ratings_movie_1.head())

ax = sns.histplot(ratings_movie_1.rating, stat='density')
ax.set(xlabel='Ratings to Toy Story', ylabel='Density')
ax.set_title('Distribution of ratings to Toy Story')
plt.show()

ax = sns.boxplot(x=ratings_movie_1.rating)
ax.set(xlabel='Ratings')
ax.set_title('Distribution of ratings to Toy Story')
plt.show()

print(f'The mean of ratings for Toy Story is {ratings_movie_1.rating.mean()}')

min_interval, max_interval = zconfint(ratings_movie_1.rating)
print(f'In Z conf the min interval to ratings for Toy Story is {min_interval} and the max interval is {max_interval}')

_, p_value = ztest(ratings_movie_1.rating, value = 3.4320503405352603)

np.random.seed(752)
temp = ratings_movie_1.sample(frac=1).rating

means = list()

def calculte_test(i):
    mean = temp[0:i].mean()
    stat, p = ztest(temp[0:i], value = 3.4320503405352603) 
    return (i, mean, p)

values = np.array([calculte_test(i) for i in range(2, len(temp))])

plt.plot(values[:,0],values[:,1])
plt.plot(values[:,0],values[:,2])
plt.hlines(y = 0.05, xmin = 2, xmax = len(temp), colors = 'r')
plt.show()
