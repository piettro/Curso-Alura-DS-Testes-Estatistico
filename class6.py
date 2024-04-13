import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import DescrStatsW
from scipy.stats import normaltest, ranksums

movies = pd.read_csv('Data/movies.csv')
ratings = pd.read_csv('Data/ratings.csv')

print(movies.query("movieId == 72226"))

ratings1 =  ratings.query("movieId == 1")
ratings593 =  ratings.query("movieId == 593")
ratings72226 =  ratings.query("movieId == 72226")
 
plt.boxplot([ratings1.rating, ratings593.rating, ratings72226.rating], labels=["Toy Story", "Silence of the Lambs,", "Fantastic Mr. Fox"])
plt.title("Distributions of ratings per movie")
plt.show()

sns.boxplot(x = "movieId", y = "rating", data = ratings.query("movieId in (1, 593, 72226)"))
plt.show()

descr_1 = DescrStatsW(ratings1.rating)
descr_593 = DescrStatsW(ratings593.rating)
compare = descr_1.get_compare(descr_593)

print(compare.summary())

descr_72226 = DescrStatsW(ratings72226.rating)
descr_593 = DescrStatsW(ratings593.rating)
compare = descr_72226.get_compare(descr_593)

print(compare.summary())

compare = descr_1.get_compare(descr_72226)

print(compare.summary())

print(ratings.query("movieId in (1, 593, 72226)").groupby("movieId").count())

_, p = normaltest(ratings1.rating)
print(p)

_, p = ranksums(ratings1.rating, ratings593.rating)
print(p)