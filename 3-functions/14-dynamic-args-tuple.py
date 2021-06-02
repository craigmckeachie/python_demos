# args array(tuple)

def sum_numbers(*args):
    sum_total = 0
    for arg in args:
        sum_total += arg
    return sum_total

print(sum_numbers(1,2,3,4,5,6))