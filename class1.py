import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_movies_imdb = pd.read_csv('Data/tmdb_5000_movies.csv')
data_movies_imdb = data_movies_imdb.query('vote_count >= 10')
print(data_movies_imdb.describe())

ratings = pd.read_csv('Data/ratings.csv')
print(ratings.describe())

ax = sns.histplot(data_movies_imdb['vote_average'])
ax.set(xlabel='Vote Average', ylabel='Frequency')
ax.set_title('Vote Average in movies from TMBD 5000')
#plt.show()

ax = sns.histplot(data_movies_imdb['vote_average'], kde= False)
ax.set(xlabel='Vote Average', ylabel='Frequency')
ax.set_title('Vote Average in movies from TMBD 5000')
#plt.show()

ax = sns.boxplot(x=data_movies_imdb['vote_average'])
ax.set(xlabel='Vote Average')
ax.set_title('Distribution of Vote Average in movies from TMBD 5000')
#plt.show()

avg_rating_per_movie = ratings.groupby('movieId')['rating'].mean()
count_ratings_per_movie = ratings.groupby('movieId').count()
movies_at_least_ten_ratings = count_ratings_per_movie.query('rating >= 10').index
avg_rating_per_movie_with_least_than_ten_ratings = avg_rating_per_movie.loc[movies_at_least_ten_ratings.values]

print(avg_rating_per_movie_with_least_than_ten_ratings.tail())

ax = sns.histplot(data=avg_rating_per_movie_with_least_than_ten_ratings, kde=False, stat='density')
ax.set(xlabel='Rating Average', ylabel='Density')
ax.set_title('Rating Average from movies in MovieLens')
plt.show()

ax = sns.boxplot(x=avg_rating_per_movie_with_least_than_ten_ratings.values)
ax.set(xlabel='Rating Average')
ax.set_title('Distribution of Rating Average in movies from MovieLens')
plt.show()

ax = sns.histplot(avg_rating_per_movie_with_least_than_ten_ratings, 
                  cumulative=True,
                  stat='percent')
ax.set(xlabel='Nota média', ylabel='Proporção acumulada de filmes')
ax.set_title('Média de votos em filmes no MovieLens')
plt.show()

ax = sns.histplot(data_movies_imdb['vote_average'], 
                  cumulative=True,
                  stat='percent')
ax.set(xlabel='Nota média', ylabel='Proporção acumulada de filmes')
ax.set_title('Média de votos em filmes no TMDB 5000')
plt.show()
