import os 

# ovning_1 måste köras innan du kan göra göra ovning_4
path = os.path.join(os.path.dirname(__file__), 'ovning_1.txt')
age = int(input("How old are you?\n"))

with open(path, "a") as f:
    f.write(f"\n{age}")