input_line = input()
best_movie = ''
max_ascii = 0
flag = False
count_movies = 0
while input_line != 'STOP':
    movie_name = input_line
    total = 0
    for i in range(len(movie_name)):
        current = ord(movie_name[i])
        if 64 < current < 96:
            current -= len(movie_name)
        elif current > 96:
            current -= len(movie_name) * 2
        total += current
    if total > max_ascii:
        best_movie = movie_name
        max_ascii = total
    count_movies += 1
    if count_movies == 7:
        flag = True
        break

    input_line = input()
if flag:
    print('The limit is reached.')
print(f'The best movie for you is {best_movie} with {max_ascii} ASCII sum.')

