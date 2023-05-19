import requests

from pprint import pprint

from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/moviemeter/'

response = requests.get(url, headers={'User-agent': 'Mozilla5.0'})

soup = BeautifulSoup(response.content, 'html.parser')

most_popular_movies = []

rating_top_10 = []

for movie in soup.find_all('td', class_='titleColumn', limit=10):

    title = movie.find('a').text

    most_popular_movies.append(title)


for rating in soup.find_all('td', class_='ratingColumn imdbRating', limit=10):

    rate = rating.find('strong')

    rating_top_10.append(rate.text)


print(f'Title: {most_popular_movies[0]} Rating: {rating_top_10[0]}')

print(f'Title: {most_popular_movies[1]} Rating: {rating_top_10[1]}')

print(f'Title: {most_popular_movies[2]} Rating: {rating_top_10[2]}')

print(f'Title: {most_popular_movies[3]} Rating: {rating_top_10[3]}')

print(f'Title: {most_popular_movies[4]} Rating: {rating_top_10[4]}')