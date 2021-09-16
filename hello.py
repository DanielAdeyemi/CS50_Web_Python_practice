name = input("Name: ")

age = int(input("Number: "))

if age < 0:
    print("Not a real age")
elif age < 21:
    print(f"No drinks for you, {name}")
else:
    print(f"Hello, {name}. Since you are {age}, what drink do you want?")
print(f"Your name starts from {name[0]}")

# info = (name, age)  # tuple
# info[0] = 'Greg'
# print(info[0])
