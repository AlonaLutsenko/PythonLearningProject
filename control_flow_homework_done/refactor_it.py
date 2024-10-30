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
        print(f"Available {source_name}(s):")
        
        for item in source:
            print(f"- {item}")
        
        selection = input(f"Select a {source_name}: ")
        if selection in source:
            return selection
        
        else:
            print(f"'{selection}' is not a valid {source_name}. Please try again.")

def movies_by_actors():
    actors_dict = {}
    for movie, cast_list in CAST.items():
        for actor in cast_list:
            if actor not in actors_dict:
                actors_dict[actor] = []
            actors_dict[actor].append(movie)
    return actors_dict



def what_to_watch():
    while True:
        choice = input("Search by genre or actor?: ").lower()

        if choice == 'genre':
            selected_genre = search(source=list(GENRES.keys()), source_name='genre')
            selected_movie = search(source=GENRES[selected_genre], source_name='movie')
            print(f"Movie to watch: '{selected_movie}'")
            break

        elif choice == 'actor':
            actors = movies_by_actors()
            selected_actor = search(source=list(actors.keys()), source_name='actor')
            actor_movie = search(source=actors[selected_actor], source_name='movie')
            print(f"Movie to watch with '{selected_actor}': '{actor_movie}'")
            break
    
        else:
            print(f"'{choice}' is not a valid option. Please select either 'genre' or 'actor'. Try again.")




what_to_watch()
