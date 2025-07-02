userinput = input("camelCase: ")

print("snake_case: ", end='')

for c in userinput:
    if c.lower() != c:
        print(f"_{c.lower()}", end="")
    else:
        print(c, end="")

print()

