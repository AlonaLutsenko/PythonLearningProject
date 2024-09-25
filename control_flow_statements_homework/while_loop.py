GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}

ACTORS = {
    'Robert De Niro': ['Meet the Parents'],
    'Ben Stiller': ['Meet the Parents'],
    'Adam Sandler': ['Anger Management'],
    'Jack Nicholson': ['Anger Management'],
    'Brendan Fraser': ['Mummy'],
    'Rachel Weisz': ['Mummy'],
    'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
    'Penelope Cruz': ['Vanilla Sky'],
    'Cameron Diaz': ['Vanilla Sky'],
    'Brad Pitt': ['Meet Joe Black'],
    'Anthony Hopkins': ['Meet Joe Black'],
    'Jeremy Renner': ['Mission Impossible']
}


def search_by_genre():
    while True:
        print("Available Genres:", list(GENRES.keys()))
        genre = input("Enter genre: ").lower()

        if genre in GENRES:
            print("Available Movies:", GENRES[genre])
            while True:
                movie = input("Enter movie: ")
                if movie in GENRES[genre]:
                    print(f"Movie to watch: {movie}. Genre: {genre}.")
                    return
                else:
                    print(f"Movie {movie} not found. Please try again.")
        else:
            print(f"Genre {genre} not found. Please try again.")


def search_by_actor():
    while True:
        print("Available Actors:", list(ACTORS.keys()))
        actor = input("Enter actor: ")

        if actor in ACTORS:
            print(f"Available movies: {ACTORS[actor]} with {actor}")
            while True:
                movie = input("Enter movie: ")
                if movie in ACTORS[actor]:
                    print(f"Movie to watch: {movie}. Starring: {actor}.")
                    return
                else:
                    print(f"Movie {movie} with actor {actor} not found. Please try again.")
        else:
            print(f"Actor {actor} not found. Please try again.")


while True:
    search_by_genre_input = input("Search by Genre (y/n)? ").lower()

    if search_by_genre_input == 'y':
        search_by_genre()
        break

    elif search_by_genre_input == 'n':
        search_by_actor_input = input("Search by Actor (y/n)? ").lower()

        if search_by_actor_input == 'y':
            search_by_actor()
            break

        else:
            print("Invalid input. Please try again.")
    else:
        print("Invalid input. Please try again.")
