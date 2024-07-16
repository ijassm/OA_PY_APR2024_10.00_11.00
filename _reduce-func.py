from functools import reduce

l = [2, 3, 4, 5]


def sum(accumulator, currentValue):
    print(accumulator, "accumulator")
    print(currentValue, "currentValue\n")
    return accumulator + currentValue


output = reduce(sum, l, 1)

print(output, "output")
