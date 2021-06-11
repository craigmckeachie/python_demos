import csv

with open("./foods.csv") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        print(row["name"], row["qty"])
