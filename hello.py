name = input("Name: ")

age = int(input("Number: "))

if age < 0:
    print("Not a real age")
elif age < 21:
    print(f"No drinks for you, {name}")
else:
    print(f"Hello, {name}. Since you are {age}, what drink do you want?")
