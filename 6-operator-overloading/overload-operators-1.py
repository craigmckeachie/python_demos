class Cart:
    def __init__(self, items):
        self.__items = items

    def __str__(self):
        return str(self.__items)

    def __add__(self, another_cart):
        return Cart(self.__items + another_cart.__items)

cart1= Cart(['coffee creamer', 'butter', 'bottled water'])
cart2 = Cart(['bread','apples', 'apple cider vinegar'])

print(cart1 + cart2)
