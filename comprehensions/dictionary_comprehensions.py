food = {
    'coffee': 'beverage',
    'pizza': 'entree',
    'cookie': 'dessert',
    'tea': 'beverage',
}

# beverages = { food:category.upper()
#               for (food, category) in food.items()
#               if category == 'beverage' }

beverages = {
    food
    for (food, category) in food.items() if category == 'beverage'
}

print(beverages)
