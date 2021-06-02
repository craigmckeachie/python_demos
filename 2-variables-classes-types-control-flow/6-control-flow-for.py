numbers = [1, 2, 3, 4, 5, 6]

print(numbers)

for number in numbers:
    # if number % 2 == 0:
    #     continue
    if number>4:
        break
    print(number)
else:
    print("sum: {}".format(sum(numbers)))
