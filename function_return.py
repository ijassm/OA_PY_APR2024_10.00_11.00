# program
l1 = [3, 4, 6, 2, 6]
l2 = [1, 3, 5, 6, 7, 8]
l3 = [1, 6, 7, 8]
# s = 0
# p = 1


# def sum(l):
#     # modify
#     global s
#     for i in l:
#         s += i


# def product(l):
#     # modify
#     global p
#     for i in l:
#         if i != 0:
#             p *= i


# # print(s)
# sum(l1)
# # print(s)

# # print(p)
# product(l1)
# # print(p)

# output = s + p

# print(output)


def sum(l):
    s = 0
    for i in l:
        s += i
    return s


def product(l):
    p = 1
    for i in l:
        if i != 0:
            p *= i
    return p


# print(sum(l1) + product(l1))

# output1 = sum(l1) + product(l1)
# output2 = sum(l2) - product(l2)
# output3 = sum(l3) / product(l3)

# print("Output of l1 - ", output1)
# print("Output of l2 - ", output2)
# print("Output of l3 - ", output3)


# def add(l):
#     s = 0
#     p = 1
#     for i in l:
#         if i != 0:
#             p *= i
#         s += i
#     return s + p

# def sub(l):
#     s = 0
#     p = 1
#     for i in l:
#         if i != 0:
#             p *= i
#         s += i
#     return s - p

# def div(l):
#     s = 0
#     p = 1
#     for i in l:
#         if i != 0:
#             p *= i
#         s += i
#     return s / p


# output1 = add(l1)

# print("Output", output1)
