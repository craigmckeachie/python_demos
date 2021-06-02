class Cart:

    def __init__(self, items):
        self.__items = items
    
    def __str__(self):
        return str(self.__items)

    def __add__(self, another_cart):
        return Cart(self.__items + another_cart.__items)

    def __mul__(self, qty_multiple):
        return Cart(list(map( lambda item: {
            'name': item['name'],
            'qty': item['qty'] * qty_multiple
        }, self.__items)))

cart = Cart([
    { 'name': 'coffee creamer', 'qty': 2 },
    { 'name': 'butter', 'qty': 3 },
    { 'name': 'bottled water', 'qty': 4 },
])

# cart2 = Cart([
#     { 'name': 'bread', 'qty': 2 },
#     { 'name': 'apples', 'qty': 2 },
#     { 'name': 'apple cider vinegar', 'qty': 2 },
# ])

print(cart * 2)