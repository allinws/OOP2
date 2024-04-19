import json
import os

# ovning_2 måste köras innan du kan göra göra ovning_5
path = os.path.join(os.path.dirname(__file__), 'ovning_2.txt')

data2 = {
  "namn": "Bob",
  "ålder": 30,
  "stad": "Göteborg"
}

with open(path, "r") as f:
    old_data = json.load(f)

with open(path, "w") as f:
    # ex_data.append(data2)
    new_data = [old_data, data2]
    json.dump(new_data, f, indent=4)