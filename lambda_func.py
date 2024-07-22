l = [2, 4, 6, 7, 9]

double_list = [i * 2 for i in l]
triple_list = [i * 3 for i in l]

# print(double_list)
# print(triple_list)


# def double(i):
#     return i * 2


# def triple(i):
#     return i * 3


# def myMap(cb, iterable):
#     output = []
#     length = len(iterable)
#     for i in range(length):
#         output.append(cb(iterable[i]))
#     return output


# def myFilter(cb, iterable):
#     output = []
#     for i in iterable:
#         if cb(i):
#             output.append(i)
#     return output


def myMap(cb, iterable):
    return [cb(i) for i in iterable]


def myFilter(cb, iterable):
    return [i for i in iterable if cb(i)]


# print(tuple(map(lambda i: i * 2, l)))
# print(tuple(map(lambda i: i * 3, l)))

print(myMap(lambda i: i * 2, l))
print(myMap(lambda i: i * 3, l))
print(myFilter(lambda i: i % 2 == 0, l))
print(list(filter(lambda i: i % 2 == 0, l)))
