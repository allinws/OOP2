import json
import os

path = os.path.join(os.path.dirname(__file__), 'users.json')
with open(path, 'r') as f:
    data = json.load(f)

count_users = len(data)

print(f"Count users: {count_users}")
print(f"Users: {json.dumps(data, indent=4)}")