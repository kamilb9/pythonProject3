import json

with open('pytania.json') as file:
    data = json.load(file)

print(data[0]['odpowiedzi'])