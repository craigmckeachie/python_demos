import csv

foods = [
    {"id": 1, "name": "apple", "qty": 2, "price": 1.20},
    {"id": 2, "name": "chicken", "qty": 4, "price": 4.30},
    {"id": 3, "name": "ice cream", "qty": 3, "price": 5.25},
    {"id": 4, "name": "soda", "qty": 1, "price": 0.99},
    {"id": 5, "name": "bacon", "qty": 2, "price": 4.55}
]

with open("./foods.csv", "w") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=list(foods[0].keys()))
    csv_writer.writeheader()
    for food in foods:
        csv_writer.writerow(food)
