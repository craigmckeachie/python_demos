import json

with open("./foods.json") as json_file:
    foods = json.load(json_file)

    for food in foods:
        print(food["name"])
