GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}

# (!) ACTORS storage does not exist anymore.
# ACTORS = {
#     'Robert De Niro': ['Meet the Parents'],
#     'Ben Stiller': ['Meet the Parents'],
#     'Adam Sandler': ['Anger Management'],
#     'Jack Nicholson': ['Anger Management'],
#     'Brendan Fraser': ['Mummy'],
#     'Rachel Weisz': ['Mummy'],
#     'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
#     'Penelope Cruz': ['Vanilla Sky'],
#     'Cameron Diaz': ['Vanilla Sky'],
#     'Brad Pitt': ['Meet Joe Black'],
#     'Anthony Hopkins': ['Meet Joe Black'],
#     'Jeremy Renner': ['Mission Impossible']
# }

CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

search_by_genre = input("Search by Genre (y/n)? ").lower()

if search_by_genre == 'y':
    print("Available Genres:")
    for genre in GENRES:
        print(genre)
    selected_genre = input("Enter genre: ").lower()
    if selected_genre in GENRES:
        print(f"Available Movies in {selected_genre}:")
        for movie in GENRES[selected_genre]:
            print(movie)
        selected_movie = input("Enter movie: ")
        if selected_movie in GENRES[selected_genre]:
            print(f"Movie to watch: {selected_movie}. Genre: {selected_genre}.")
        else:
            print("Movie not found.")
    else:
        print("Genre not found.")
# end first step

elif search_by_genre == 'n':
    search_by_actor = input("Search by Actor (y/n)? ").lower()
    if search_by_actor == 'y':

        actor_list = []
        for actors in CAST.values():
            actor_list.extend(actors)
        unique_actors = list(set(actor_list))
        print("Available Actors:")
        for actor in sorted(unique_actors):
            print(actor)

        selected_actor = input("Enter actor: ")

        movies = []
        for movie, actors in CAST.items():
            if selected_actor in actors:
                movies.append(movie)
        if movies:
            print(f"Available movies with {selected_actor}: {', '.join(movies)}")
        else:
            print(f"{selected_actor} not found.")

    else:
        print("Error: Incorrect input for actor search.")
else:
    print("Error: Invalid input for genre search.")