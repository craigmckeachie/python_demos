cart = [
    [ 'Coffee', 7.99, 2 ],
    [ 'Bread', 2.99, 1 ],
    [ 'Apple', 0.99, 2 ],
    [ 'Milk', 4.99, 1 ],
    [ 'Cola', 1.99, 4 ],
]

cart_items_one_count = [ name for (name, price, qty) in cart if qty == 1]

print(cart_items_one_count)


