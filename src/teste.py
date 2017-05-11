import json
from random import randint
with open('colors.json') as data_file:
    data = json.load(data_file)

print(data['color'][randint(1,len(data['color']))])
