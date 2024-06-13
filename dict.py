# l = ["Tokiyo", 25, "London"]

# person = {
#     "name": "Tokiyo",
#     "age": 25,
#     "city": "London",
# }

# # print(type(l))
# # print(type(person))

# person["age"] = person["age"] + 1

# person["skills"] = ["PYTHON", "JAVA", "C", "C++"]

# print(person["name"])
# print(person["age"])
# print(person["city"])
# print(person["skills"])


fruits = ["apple", "orange", "kiwi"]
persons = [
    {
        "name": "Benjamine",
        "age": 21,
        "city": "London",
    },
    {
        "name": "Sakthinarayan",
        "age": 20,
        "city": "Tokyo",
    },
]


isAdd = True

while isAdd:
    isAdd = input("Enter you Y/N to add new person : ")
    if isAdd == "Y":
        person = {
            "name": input("Enter name: "),
            "age": int(input("Enter age: ")),
            "city": input("Enter city: "),
        }
        persons.append(person)
    elif isAdd == "N":
        isAdd = False
        break
    else:
        print("Invalid input please try again")


for i in persons:
    print(i, "\n")
