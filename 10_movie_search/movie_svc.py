import collections
import requests

MovieResult = collections.namedtuple(
    'MovieResult', 
     "imdb_code, title, director, keywords, duration, genres, rating, year, imdb_score")


def find_movies(search_text):
    url = 'https://movieservice.talkpython.fm/api/search/{}'.format(search)

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    movies = [
        MovieResult(**md)
        for md in movies_list
    ]

    return movies
