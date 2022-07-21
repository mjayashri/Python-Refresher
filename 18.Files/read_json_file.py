import json

with open("friends.json") as file:
    file_contents = json.load(file)  # reads file and turns into dictionary

print(file_contents["friends"][0])

cars = [
    {'make':'Ford', 'model':'Fiesta'},
    {'make':'Ford', 'model':'Focus'}
]
# json dump
with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)

my_json_String = '[{"name":"Alfa Romeo", "released":1950}]'

incorrect_car = json.loads(my_json_String)

print(incorrect_car[0]['name'])
