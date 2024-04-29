a = 625
b = 4555
c = 70

print("a -", a)
print("b -", b)
print("c -", c)
print()

if a > b and a > c:
    print("a is greater than b and c")
    if b < c:
        print("b is smaller than a and c")
    else:
        print("c is smaller than a and b")
elif b > c:
    print("b is greater than a and c")
    if a < c:
        print("a is smaller than b and c")
    else:
        print("c is smaller than a and b")
else:
    print("c is greater than b and a")
    if a < b:
        print("a is smaller than b and c")
    else:
        print("b is smaller than a and c")
    
    
