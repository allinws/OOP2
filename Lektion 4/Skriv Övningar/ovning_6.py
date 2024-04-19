import csv

new_list = []
with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        new_list.append(row)

new_list.append(["Charlie","35","Malmö"])

with open('people.csv', mode='w') as file:
    writer = csv.writer(file)
        
    for row in new_list:
        writer.writerow(row)