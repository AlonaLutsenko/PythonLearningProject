GENRES = {
    'Action': ['Die Hard', 'Mad Max'],
    'Comedy': ['Superbad', 'Groundhog Day'],
    'Drama': ['The Shawshank Redemption', 'Forrest Gump'],
}

CAST = {
    'Die Hard': ['Bruce Willis', 'Alan Rickman'],
    'Mad Max': ['Tom Hardy', 'Charlize Theron'],
    'Superbad': ['Jonah Hill', 'Michael Cera'],
    'Groundhog Day': ['Bill Murray', 'Andie MacDowell'],
    'The Shawshank Redemption': ['Tim Robbins', 'Morgan Freeman'],
    'Forrest Gump': ['Tom Hanks', 'Robin Wright'],
}

PG = {
    13: {'Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
    16: {'Vanilla Sky'}
}

def get_user_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def filter_movies_by_age(age):
    restricted_movies = set()
    for pg_age, movies in PG.items():
        if age < pg_age:
            restricted_movies.update(movies)
    return restricted_movies

def is_movie_allowed(movie, restricted_movies):
    return movie not in restricted_movies

def filter_genre_movies(movies, restricted_movies):
    allowed_movies = []
    for movie in movies:
        if is_movie_allowed(movie, restricted_movies):
            allowed_movies.append(movie)
    return allowed_movies


def prepare():
    age = get_user_age()
    restricted_movies = filter_movies_by_age(age)
    new_genres = {}

    for genre, movies in GENRES.items():
        filtered_movies = filter_genre_movies(movies, restricted_movies)
        if filtered_movies:
            new_genres[genre] = filtered_movies

    return new_genres



filtered_genres = prepare()
print(filtered_genres)