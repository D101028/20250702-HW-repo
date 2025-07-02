userinput = input("Greeting: ").strip()

start = userinput.split()[0].lower()

if start[:5] == "hello":
    print("$0")
elif start[0] == "h":
    print("$20")
else:
    print("$100")
