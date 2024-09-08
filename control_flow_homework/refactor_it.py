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


def search(source, source_name='genre'):
    while True:
        print(f"Available {source_name}(s): {', '.join(source)}")
        selection = input(f"Please select a {source_name}: ").strip()
        if selection in source:
            return selection
        else:
            print(f"{selection} is not a valid {source_name}. Try again.")


def movies_by_actors(cast):
    actors = {}
    for movie, movie_cast in cast.items():
        for actor in movie_cast:
            if actor not in actors:
                actors[actor] = []
            actors[actor].append(movie)
    return actors


def pick_movie_by_genre():
    genre = search(source=list(GENRES.keys()), source_name='genre')
    movie = search(source=GENRES[genre], source_name='movie')

    return movie


def pick_movie_by_actor():
    actors = movies_by_actors(CAST)
    actor = search(source=list(actors.keys()), source_name='actor')
    movie = search(source=actors[actor], source_name='movie')

    return movie


def main():
    print("Welcome to the Movie Picker!")
    choice = input("Do you want to search by genre or by actor? ").strip().lower()

    if choice == 'genre':
        selected_movie = pick_movie_by_genre()
    elif choice == 'actor':
        selected_movie = pick_movie_by_actor()
    else:
        print("Invalid choice, defaulting to genre search.")
        selected_movie = pick_movie_by_genre()

    print(f"You selected the movie: {selected_movie}")

main()