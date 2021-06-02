from functools import partial

def add(x,y): return x + y

print(add(1,2))

add2 = partial(add, 2)

print(add2(10))
