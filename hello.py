names = []  # empty list of names
ages = set()  # create an empty set

info = {}  # define a dictionary

for i in range(3):
    name = input("Name: ")
    names.append(name)  # add element to the end of the list

    age = int(input("Age: "))
    ages.add(age)

    info[name] = age

    if age < 0:
        print("Not a real age")
    elif age < 21:
        print(f"No drinks for you, {name}")
    else:
        print(f"Hello, {name}. Since you are {age}, what drink do you want?")

names.sort()
print(names)
print(f"We have {len(ages)} different ages, they are: ", end="")
print(ages)

for name in info:
    print(info[name])

# info = (name, age)  # tuple
# info[0] = 'Greg' - impossible since tuples are immutable
# print(info[0])
