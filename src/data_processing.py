import pandas as pd

movies = pd.read_csv("../data/movies.csv")
ratings = pd.read_csv("../data/ratings.csv")

print(movies.head())
print(ratings.head())

merged_data = pd.merge(ratings, movies, on="movieId")

print(merged_data.head())

user_movie_matrix = merged_data.pivot_table(
    index="userId", columns="movieId", values="rating"
).fillna(0)

print(user_movie_matrix.head())
