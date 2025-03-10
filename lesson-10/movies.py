import requests
import random

API_KEY = "65c2857031b0a4911a64cd5a44407cd4"
BASE_URL = "https://api.themoviedb.org/3"

genre_url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
genre_response = requests.get(genre_url).json()
genres = {g["name"].lower(): g["id"] for g in genre_response["genres"]}

user_genre = input("Enter a movie genre: ").strip().lower()

if user_genre in genres:
    genre_id = genres[user_genre]
    movie_url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    movie_response = requests.get(movie_url).json()

    if movie_response["results"]:
        random_movie = random.choice(movie_response["results"])
        print(f"Recommended movie: {random_movie['title']}")
    else:
        print("No movies found for this genre.")
else:
    print("Invalid genre. Try again.")
