# functions are objects
def do_it():
    print("did it")

print(type(do_it))
# <class 'function'>

do_it2= do_it
print(type(do_it2))
# <class 'function'>

do_it2()
# did it

# function names
print(do_it.__name__)
print(do_it2.__name__)
# do_it
# do_it

# functions as objects
def double(x): return x * 2

numbers = [1,2,3,4,5]
numbersDoubled = list(map(double, numbers))
print(numbersDoubled)
