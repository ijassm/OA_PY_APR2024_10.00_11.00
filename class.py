class Student:
    name = ""
    age = 0
    location = ""
    registerNumber = 0
    phoneNumber = 0
    countryCode = 0
    email = ""

    def getDetails(self):
        print(self)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Location :", self.location)
        print("Country Code :", self.countryCode)
        print("Phone Number :", self.phoneNumber)
        print("Email :", self.email)
        print("registerNumber :", self.registerNumber)


obj1 = Student()
obj2 = Student()
obj3 = obj1

obj3.age = 25


obj1.name = "Sakthi Narayanan"
# obj1.age = 18
obj1.location = "US"
obj1.countryCode = "+1"
obj1.phoneNumber = 6369285544
obj1.email = "sakthinaran30@gmail.com"
obj1.registerNumber = 13100175
obj1.name = "Sakthi Narayanan"

obj2.name = "Benjamine"
obj2.age = 17
obj2.location = "India"
obj2.countryCode = "+91"
obj2.phoneNumber = 9944060314
obj2.email = "benjamine2712@gmail.com"
obj2.registerNumber = 12450


obj1.getDetails()
# Student.getDetails(obj1)

# print(obj1)
# print("Name :", obj1.name)
# print("Age :", obj1.age)
# print("Location :", obj1.location)
# print("Country Code :", obj1.countryCode)
# print("Phone Number :", obj1.phoneNumber)
# print("Email :", obj1.email)
# print("registerNumber :", obj1.registerNumber)

print("")

obj2.getDetails()
# print(obj2)
# print("Name :", obj2.name)
# print("Age :", obj2.age)
# print("Location :", obj2.location)
# print("Country Code :", obj2.countryCode)
# print("Phone Number :", obj2.phoneNumber)
# print("Email :", obj2.email)
# print("registerNumber :", obj2.registerNumber)

print()

obj3.getDetails()
# print(obj3)
# print("Name :", obj3.name)
# print("Age :", obj3.age)
# print("Location :", obj3.location)
# print("Country Code :", obj3.countryCode)
# print("Phone Number :", obj3.phoneNumber)
# print("Email :", obj3.email)
# print("registerNumber :", obj3.registerNumber)


# print(obj1 is obj2)
# print(id(obj1))
# print(id(obj2))
