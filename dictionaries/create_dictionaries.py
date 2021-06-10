# person = dict(
#     first_name="Sally",
#     last_name="Thompkins"
# )

# person = {
#     "first_name": "Sally",
#     "last_name": "Thompkins"
# }

# person = dict([
#     ("first_name", "Sally"),
#     ("last_name", "Thompkins")
# ])

# person = dict(zip(
#     ["first_name", "last_name"],
#     ["Sally", "Thompkins"]
# ))

# print(person)

# contest_places = dict.fromkeys(["first", "second", "third"])
contest_places = dict.fromkeys(["first", "second", "third"], "default")
print(contest_places)
