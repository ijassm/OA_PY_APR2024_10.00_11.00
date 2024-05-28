# storings collections of data

# a = 1
# b = 2
# c = 3

# print(a)
# print(b)
# print(c)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# access
print("Positive index🎈")

print("l[0]", l[0])
print("l[1]", l[1])
print("l[2]", l[2])
print("l[3]", l[3])
print("l[4]", l[4])
print("l[5]", l[5])
print("l[6]", l[6])
print("l[7]", l[7])

print("Negative index🎈")

print("l[-1]", l[-1])
print("l[-2]", l[-2])
print("l[-3]", l[-3])
print("l[-4]", l[-4])
print("l[-5]", l[-5])
print("l[-6]", l[-6])
print("l[-7]", l[-7])
print("l[-8]", l[-8])
print("l[-9]", l[-9])

# mutable
l[0], l[-1] = l[-1], l[0]


# methods

l.append(10)
print(l.count(10))
print(l.copy())


print(l)
print(type(l))

# iterable

# for i in range(len(l)):
#     # print(f"Index {i} : {l[i]}")
#     print("Index {:02d} : {:03d}".format(i, l[i]))

# type cast

# a = "hello"
# b = list(a)

# b[0] = "H"

# a = ""

# for i in b:
#     a += i


# print(a)
# print(b)

# Task
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = []
# odd = []
