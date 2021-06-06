# class ParentA:

#     def __init__(self):
#         print("Parent A Contructor")


# class Child(ParentA):

#     def __init__(self):
#         print('Child Constructor')
#         super().__init__()


# child = Child()

# print(Child.__mro__)

#######
# add super calls in Parent A and Parent B to see everything execute
# class ParentA:

#     def __init__(self):
#         print("Parent A Contructor")
#         super().__init__()


# class ParentB:

#     def __init__(self):
#         print("Parent B Contructor")
#         super().__init__()


# class Child(ParentB, ParentA):

#     def __init__(self):
#         print('Child Constructor')
#         super().__init__()


# child = Child()

# print(Child.__mro__)


########

# class GrandparentA:
#     def __init__(self):
#         print("Grandparent A Contructor")
#         super().__init__()


# class GrandparentB:
#     def __init__(self):
#         print("Grandparent B Contructor")
#         super().__init__()


# class ParentA(GrandparentA):

#     def __init__(self):
#         print("Parent A Contructor")
#         super().__init__()


# class ParentB(GrandparentB):

#     def __init__(self):
#         print("Parent B Contructor")
#         super().__init__()


# class Child(ParentB, ParentA):

#     def __init__(self):
#         print('Child Constructor')
#         super().__init__()


# child = Child()

# print(Child.__mro__)


###############

class Grandparent:
    def __init__(self):
        print("Grandparent Contructor")
        super().__init__()

    def do_it(self):
        print("Grandparent DoIt")


class ParentA(Grandparent):

    def __init__(self):
        print("Parent A Contructor")
        super().__init__()

    def do_it(self):
        print("ParentA DoIt")


class ParentB(Grandparent):

    def __init__(self):
        print("Parent B Contructor")
        super().__init__()


class Child(ParentB, ParentA):

    def __init__(self):
        print('Child Constructor')
        super().__init__()


child = Child()
child.do_it()

print(Child.__mro__)
