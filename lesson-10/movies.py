import requests
import random

API_KEY = "65c2857031b0a4911a64cd5a44407cd4"
BASE_URL = "https://api.themoviedb.org/3/discover/movie"

genre = input("Enter movie genre (e.g., Action, Comedy, Drama): ").lower()

# Mapping genres to their TMDb IDs
GENRE_IDS = {
    "action": 28,
    "comedy": 35,
    "drama": 18,
    "horror": 27,
    "romance": 10749
}

if genre not in GENRE_IDS:
    print("Invalid genre! Please choose from Action, Comedy, Drama, Horror, Romance.")
else:
    params = {
        "api_key": API_KEY,
        "with_genres": GENRE_IDS[genre],
        "language": "en-US",
        "sort_by": "popularity.desc"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        movies = data.get("results", [])

        if movies:
            movie = random.choice(movies)
            print(f"🎬 Recommended Movie: {movie['title']} ({movie['release_date'][:4]})")
            print(f"⭐ Rating: {movie['vote_average']}")
            print(f"📜 Overview: {movie['overview']}")
        else:
            print("No movies found for this genre.")
    except requests.exceptions.RequestException as err:
        print(f"Error fetching movie data: {err}")
