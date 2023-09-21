import sys

count_movies = int(input())

name_of_movie_max = ''
name_of_movie_min = ''
max_rating = -sys.maxsize
min_rating = sys.maxsize
total_rating = 0

for _ in range(count_movies):
    name_of_movie = input()
    rating = float(input())
    total_rating += rating
    if rating > max_rating:
        max_rating = rating
        name_of_movie_max = name_of_movie
    if rating < min_rating:
        min_rating = rating
        name_of_movie_min = name_of_movie

average_rating = total_rating / count_movies

print(f'{name_of_movie_max} is with highest rating: {max_rating:.1f}')
print(f'{name_of_movie_min} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')
