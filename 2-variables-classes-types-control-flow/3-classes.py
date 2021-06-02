class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name
        # return "{} {}".format(self.first_name, self.last_name)

    def __repr__(self):
        return "Person: {} {}".format(self.first_name, self.last_name)


        

p = Person('Teddy', "Riley")

print(p.first_name)
print(p.last_name)
print(p.get_full_name())
print(p)
