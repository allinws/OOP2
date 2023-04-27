import requests
from bs4 import BeautifulSoup
import pprint

url = "https://www.reddit.com/r/sweden/"
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.content, "html.parser")

posts = []
for post in soup.find_all("div", class_="Post"):
    title = post.find("h3", class_="_eYtD2XCVieq6emjKBH3m").text
    comments = post.find("span", class_="FHCV02u6Cp2zYL0fhQPsO").text
    number = int(comments.split()[0])
    obj = {'title': title, 'comments_count': number}
    posts.append(obj)

posts = sorted(posts, key=lambda x: x['comments_count'], reverse=True)

pprint.pprint(posts, indent=4)