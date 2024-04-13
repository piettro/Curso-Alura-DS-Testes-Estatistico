import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_movies_imdb = pd.read_csv('Data/tmdb_5000_movies.csv')
data_movies_imdb_more_than_ten_votes = data_movies_imdb.query('vote_count >= 10')
data_movies_imdb_more_than_zero_budget = data_movies_imdb.query('budget > 0')

print(data_movies_imdb.describe())

ratings = pd.read_csv('Data/ratings.csv')
print(ratings.describe())

ax = sns.histplot(data_movies_imdb_more_than_ten_votes['vote_count'], stat='density')
ax.set(xlabel='Vote Count', ylabel='Density')
ax.set_title('Vote Count in movies from TMDB 5000 with more than 10 votes')
plt.show()

ax = sns.histplot(data_movies_imdb_more_than_zero_budget['budget'], stat='density')
ax.set(xlabel='Budget', ylabel='Density')
ax.set_title('Budget in moview from TMDB 5000')
plt.show()

ax = sns.histplot(data_movies_imdb.query("runtime>0").runtime.dropna(), stat='density')
ax.set(xlabel='Run time', ylabel='Density')
ax.set_title('Run time in movies from TMDB 5000')
plt.show()

ax = sns.histplot(data_movies_imdb.query("runtime>0").runtime.dropna(), stat='density',cumulative=True)
ax.set(xlabel='Run time', ylabel='Density')
ax.set_title('Cumulative Run time in movies from TMDB 5000')
plt.show()

print(data_movies_imdb.query("runtime>0").runtime.dropna().quantile(q=0.8))