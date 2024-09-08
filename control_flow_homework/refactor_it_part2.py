PG = {
    13: {'Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
    16: {'Vanilla Sky'}
}

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

def get_user_age():
    while True:
        try:
            age = int(input("Please enter your age: ").strip())
            return age
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def prepare(genres, pg_rate):
    new_genres = {}
    for genre, movies in genres.items():
        filtered_movies = []
        for movie in movies:
            allowed = True
            for age_limit, restricted_movies in PG.items():
                if pg_rate < age_limit and movie in restricted_movies:
                    allowed = False
                    break
            if allowed:
                filtered_movies.append(movie)
        if filtered_movies:
            new_genres[genre] = filtered_movies
    return new_genres


def movies_by_actors(cast, pg_rate):
    actors = {}
    for movie, movie_cast in cast.items():
        allowed = True
        for age_limit, restricted_movies in PG.items():
            if pg_rate < age_limit and movie in restricted_movies:
                allowed = False
                break
        if allowed:
            for actor in movie_cast:
                if actor not in actors:
                    actors[actor] = []
                actors[actor].append(movie)
    return actors


def search(source, source_name='genre'):
    while True:
        print(f"Available {source_name}(s): {', '.join(source)}")
        selection = input(f"Please select a {source_name}: ").strip()
        if selection in source:
            return selection
        else:
            print(f"{selection} is not a valid {source_name}. Try again.")


def pick_movie_by_genre(genres):
    genre = search(source=list(genres.keys()), source_name='genre')
    movie = search(source=genres[genre], source_name='movie')

    return movie


def pick_movie_by_actor(cast, pg_rate):
    actors = movies_by_actors(cast, pg_rate)
    actor = search(source=list(actors.keys()), source_name='actor')
    movie = search(source=actors[actor], source_name='movie')

    return movie


def main():
    print("Welcome to the Movie Picker!")
    user_age = get_user_age()
    filtered_genres = prepare(GENRES, user_age)

    if not filtered_genres:
        print("Sorry, there are no movies available for your age.")
        return

    choice = input("Do you want to search by genre or by actor? ").strip().lower()

    if choice == 'genre':
        selected_movie = pick_movie_by_genre(filtered_genres)
    elif choice == 'actor':
        selected_movie = pick_movie_by_actor(CAST, user_age)
    else:
        print("Invalid choice, defaulting to genre search.")
        selected_movie = pick_movie_by_genre(filtered_genres)

    print(f"You selected the movie: {selected_movie}")

main()