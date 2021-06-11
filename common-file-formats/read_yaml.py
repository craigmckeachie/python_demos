import yaml


with open("./foods.yml") as yml_file:
    foods = yaml.load(yml_file, Loader=yaml.SafeLoader)

    for food in foods:
        print(food["name"])
