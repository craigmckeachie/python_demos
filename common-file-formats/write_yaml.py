import yaml

foods = [
    {"id": 1, "name": "apple", "qty": 2, "price": 1.20},
    {"id": 2, "name": "chicken", "qty": 4, "price": 4.30},
    {"id": 3, "name": "ice cream", "qty": 3, "price": 5.25},
    {"id": 4, "name": "soda", "qty": 1, "price": 0.99},
    {"id": 5, "name": "bacon", "qty": 2, "price": 4.55}
]

with open("./foods.yml", "w") as yaml_file:
    yaml_file.write(yaml.dump(foods))
