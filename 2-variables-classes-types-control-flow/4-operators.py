# if either is true then true with or
print(True or False)
print(True or True)
print(False or True)


# if either are false then false with and
print(False and True)
print(True and False)

# negate
print(not True)
print(not False)

# 2 is truthy
# 0 is falsy
print(2 and 0)
print(2 or 0)

print(2)
print(0)
print(2 <= 5)
print(2 == 2)
print(2 == "2")
# no coercion strongly typed


print(type(2))
print(type(2.))

# one exception where coercion happens
print (2 == 2.)


