userinput = input("Input: ")
print("Output: ", end="")

for c in userinput:
    if c.lower() in "aeiou":
        continue
    else:
        print(c, end="")

print()