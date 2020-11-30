import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult', 
     "imdb_code, title, director, keywords, duration, genres, rating, year, imdb_score")

search = 'capital'
url = 'https://movieservice.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)
resp.raise_for_status()

print(resp.status_code)

print(resp.text)

movie_data = resp.json()
movies_list = movie_data.get('hits')

# print(type(movies), movies)

movies = []
for md in movies_list:
    