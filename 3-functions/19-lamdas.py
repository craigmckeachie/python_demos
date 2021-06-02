def double(x): return x * 2

numbers = [1, 2, 3, 4, 5]
print(list(map(double, numbers)))

##
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, numbers)))

##

numbers = [1, 2, 3, 4, 5]
# violation of PEP-8
double = lambda x: x * 2;
print(list(map(double, numbers)))

## list comprehension
numbers = [1, 2, 3, 4, 5]
print([x * 2 for x in numbers])