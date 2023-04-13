import os

path = os.path.join(os.path.dirname(__file__), 'name_list.txt')
with open(path, 'r') as f:
    data = f.read()

name_list = data.split('\n')
name_count = len(name_list)

print(f"Names: {name_list}")
print(f"Count of names: {name_count}")