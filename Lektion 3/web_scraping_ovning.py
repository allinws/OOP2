import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

job_data = []

jobs = soup.find_all("div", class_ = "card-content")

for job in jobs:
    title = job.find("h2", class_ = "title").text.strip()
    company = job.find("h3", class_ = "company").text.strip()
    date = job.find("p", class_ = "is-small").text.strip()
    links = job.find_all("a", class_ = "card-footer-item")
    apply_link = links[1]['href']
    job_dict = {
        'title': title,
        'company': company,
        'date': date,
        'apply_link': apply_link,
    }
    job_data.append(job_dict)

pprint(job_data)
