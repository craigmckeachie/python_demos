# Overload __contains__ and Iterables __iter__


class Cart:
    def __init__(self, items):
        self.__items = items

    def __contains__(self, itemName):
        return len([item
                    for item in self.__items
                    if item['name'] == itemName]) > 0

    def __iter__(self):
        return iter(self.__items)


cart = Cart(
    [{'name': 'coffee creamer', 'qty': 2},
     {'name': 'butter', 'qty': 2},
     {'name': 'bottled water', 'qty': 6}])

print('butter' in cart)

for item in cart:
    print(item['name'])
