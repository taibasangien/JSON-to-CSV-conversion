mport json
import csv


with open ('example_1.json', 'r') as f:
    data = json.load(f)
    names = data['names']

with open ('example_1.csv', 'w') as f:
    fieldnames = names[0].keys()
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for name in names:
        writer.writerow(name)
        
