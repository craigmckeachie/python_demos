# creating
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

empty_list = []
print(empty_list)
print(type(empty_list))


# mutating
colors = ['red', 'white', 'blue']
colors.append('orange')
colors.insert(1, 'yellow')
colors.remove('blue')

last_color = colors.pop()
print(last_color)
print(colors)

colors.clear()
print(len(colors))

# sorting
numbers = [1, 4, 5, 3, 2]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# reverses current order, does not sort
numbers = [1, 4, 5, 3, 2]
numbers.reverse()
print(numbers)

# sorting objects
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return "Person: {} {}".format(self.fname, self.lname)

people = [
    Person("Bob", "Smith"),
    Person("Tim", "Johnson"),
    Person("Mike", "Collins")
]    

people.sort(key=lambda p: p.lname)
print(people)

people.sort(key=lambda p: p.lname, reverse=True)
print(people)

# map, filter, reduce

nums = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

print(map(square, nums))    
print(list(map(square, nums))) 
print(nums)

people = [
    ("Bob", 34),
    ("Jen", 13),
    ("Abe", 24),
    ("Karen", 56)
]

# TypeError: 'tuple' object is not callable happens if commas after each tupple are omitted
print(list(filter(lambda p: p[1] > 30, people)))


from functools import reduce
nums = [1, 2, 3, 4, 5]

# sum = reduce(lambda acc, current: acc + current, nums)
# print(sum)

def sum(total, next_val):
    print("total: {}, next val: {}".format(total, next_val))
    return total + next_val

sum = reduce(sum, nums)

# slicing
colors = ["red", "blue", "green", "yellow"]
print(colors[1])
print(colors[1:])
print(colors[:1])
print(colors[1:3])
print(colors)

# iteration
for color in colors:
    print(color)

# enumerate
for index, color in enumerate(colors):
    print(index, color)    











