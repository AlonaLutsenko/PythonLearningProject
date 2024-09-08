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

search_by_genre = input("Search by Genre (y/n)? ").lower()

if search_by_genre == 'y':
    print("Available Genres:", list(GENRES.keys()))

    genre = input("Enter genre: ").lower()

    if genre in GENRES:
        print("Available Movies:", GENRES[genre])

        movie = input("Enter movie: ")

        if movie in GENRES[genre]:
            print(f"Movie to watch: {movie}. Genre: {genre}.")
        else:
            print("Error: This movie is not available in the selected genre.")
    else:
        print("Error: This genre is not available.")

elif search_by_genre == 'n':
    search_by_actor = input("Search by Actor (y/n)? ").lower()

    if search_by_actor == 'y':
        print("Available Actors:", list(ACTORS.keys()))

        actor = input("Enter actor: ")

        if actor in ACTORS:
            print(f"Available movies: {ACTORS[actor]} with {actor}")

            movie = input("Enter movie: ")

            if movie in ACTORS[actor]:
                print(f"Movie to watch: {movie}. Starring: {actor}.")
            else:
                print("Error: This movie is not available for the selected actor.")
        else:
            print("Error: This actor is not available.")

    else:
        print("Error: You chose neither genre nor actor.")
else:
    print("Error: Invalid input for genre search.")
