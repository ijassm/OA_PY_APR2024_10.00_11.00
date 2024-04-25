a = 1
b = str(a)
c = float(a)
d = complex(a)
e = bool(a)

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)

##Falsy values
print(bool(0))
print(bool(-0))
print(bool(0j))
print(bool(0.0))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(""), "--")
print(bool(" "), "--")
##print(0.1 > 0)
##print(0.1 == 0)

##Truthy values
print(bool(2-5))
print(bool(0.5))
print(bool("0"))
