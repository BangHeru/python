import json

with open('rute.json') as data_file:    
    data = json.load(data_file)
    data = json.dumps(data,sort_keys=True)

print(data['Arad'])