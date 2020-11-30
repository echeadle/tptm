import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult', 
     "imdb_code, title, director, keywords, duration, genres, rating, year, imdb_score")

search = input("What movie do you want to search for? ")

url = 'https://movieservice.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)
resp.raise_for_status()

# print(resp.status_code)

# print(resp.text)

movie_data = resp.json()
movies_list = movie_data.get('hits')

# print(type(movies), movies)

# movies = []
# for md in movies_list:
#     m = MovieResult(
#         imdb_code = md.get('imdb_code'),
#         title = md.get('title'),
#         director = md.get('director'),
#         keywords = md.get('keywords'),
#         duration = md.get('duration'),
#         genres = md.get('genres'),
#         rating = md.get('rating', 0),
#         year = md.get('year', 0),
#         imdb_score = md.get('imdb_score', 0.0)
#     )
#     movies.append(m)

# movies = []
# for md in movies_list:
#     m = MovieResult(**md)
#     movies.append(m)

movies = [
    MovieResult(**md)
    for md in movies_list
]
    

print("Found {} movies for search {}".format(len(movies),search))
for m in movies:
    print("{} -- {}".format(m.year, m.title))
