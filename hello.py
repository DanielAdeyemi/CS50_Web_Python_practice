names = []  # empty list of names
ages = set()

for i in range(3):
    name = input("Name: ")
    names.append(name)  # add element to the end of the list

    age = int(input("Age: "))

    if age < 0:
        print("Not a real age")
    elif age < 21:
        print(f"No drinks for you, {name}")
    else:
        print(f"Hello, {name}. Since you are {age}, what drink do you want?")

names.sort()
print(names)

# info = (name, age)  # tuple
# info[0] = 'Greg'
# print(info[0])
