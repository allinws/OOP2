import json
import csv
import json
from pathlib import Path
import sys
import os

filename = 'hej.json'
current_path = os.path.join(os.path.dirname(__file__), filename)

""" CREATE INTIAL FILE """

data = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Physics", "Programming"]
}

with open(f"{current_path}", "w") as outfile:
    json.dump(data, outfile, indent=2)


""" ADD NEW DATA TO FILE """


new_data = {
    "name": "Bob",
    "age": 30,
    "is_student": False,
    "courses": ["Chemistry", "Biology", "Geology"]
}

with open(f"{current_path}", "r") as infile:
    existing_data = json.load(infile)

existing_data_list = [existing_data, new_data]

with open(f"{current_path}", "w") as outfile:
    json.dump(existing_data_list, outfile, indent=2)

