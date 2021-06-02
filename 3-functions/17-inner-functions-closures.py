# nested function
# def outer():
#     print('outer')

#     def inner():
#         print('inner')
    
#     inner()

# outer()


# nest function that returns inner function
# def outer():
#     print('outer')

#     def inner():
#         print('inner')
    
#     return inner

# fn = outer()
# fn()


# reading a closure variable
# def outer():
#     print('outer')
#     number = 2

#     def inner():
#         print('inner')
#         print(number)
    
#     return inner

# inner_fn = outer()
# inner_fn()
# print(inner_fn.__closure__)
# print(inner_fn.__closure__[0].cell_contents)


# mutating a closure variable (nonlocal)
def outer():
    number = 2

    def update_number():
        nonlocal number
        number = number + 1

    def print_number(): print(number)

    return (update_number, print_number)

(update_fn, print_fn) = outer()

print_fn()
update_fn()
print_fn()