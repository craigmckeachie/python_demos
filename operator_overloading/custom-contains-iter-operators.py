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

    def __gt__(self, another_cart):

        print('called greater than')

        left = sum(item['qty'] for item in self.__items)
        right = sum(item['qty'] for item in another_cart.__items)

        return left > right
        
    # def __lt__(self, another_cart):

    #     left = sum(item['qty'] for item in self.__items)
    #     right = sum(item['qty'] for item in another_cart.__items)

    #     return left < right

    def __getitem__(self, index):
        return self.__items[index]

    def __len__(self):
        return len(self.__items)

    def __contains__(self, itemName):
        return len([item
                        for item in self.__items
                        if item['name'] == itemName
                    ]) > 0

    def __iter__(self):
        return iter(self.__items)

cart = Cart([
    { 'name': 'coffee creamer', 'qty': 2 },
    { 'name': 'butter', 'qty': 3 },
    { 'name': 'bottled water', 'qty': 4 },
])

# cart2 = Cart([
#     { 'name': 'bread', 'qty': 1 },
#     { 'name': 'apples', 'qty': 5 },
#     { 'name': 'apple cider vinegar', 'qty': 4 },
# ])

# print('butter' in cart)

for item in cart:
    print(item['name'])