import os

filename = 'hej.txt'
current_path = os.path.join(os.path.dirname(__file__), filename)

data = "Detta är en textsträng."

with open(current_path, "w") as outfile:
    outfile.write(data)

with open(current_path, "r") as infile:
    existing_data = infile.read()

new_data = "Detta är en ny textsträng."

with open(current_path, "w") as outfile:
    outfile.write(existing_data + "\n" + new_data)