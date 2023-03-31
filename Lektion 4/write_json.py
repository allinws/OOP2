import json

data = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Physics", "Programming"]
}

with open("data.json", "w") as outfile:
    json.dump(data, outfile, indent=2)