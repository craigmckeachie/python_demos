name = 'John'

# Python 3.6+
print(f"Hello! {name}")
print("Hello! {}".format(name))

# for User-supplied input
# see https://realpython.com/python-string-formatting/
from string import Template
name = input("Type your name: ")
print(Template("Hello! $first_name").substitute(first_name=name))

