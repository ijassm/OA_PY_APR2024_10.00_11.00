# def first():
#     print("first")


# def second():
#     print("second")
#     first()


# def third():
#     print("third")
#     second()


# third()


def recursion(n):
    if n == 0:
        return
    recursion(n - 1)
    print(n)


recursion(1000)
