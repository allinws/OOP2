import json
import csv
import json
from pathlib import Path
import sys

current_path = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent

""" CREATE INTIAL FILE """

data = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Physics", "Programming"]
}

with open(f"{current_path}/data.json", "w") as outfile:
    json.dump(data, outfile, indent=2)


""" ADD NEW DATA TO FILE """


new_data = {
    "name": "Bob",
    "age": 30,
    "is_student": False,
    "courses": ["Chemistry", "Biology", "Geology"]
}

with open(f"{current_path}/data.json", "r") as infile:
    existing_data = json.load(infile)

existing_data_list = [existing_data, new_data]

with open(f"{current_path}/data.json", "w") as outfile:
    json.dump(existing_data_list, outfile, indent=2)