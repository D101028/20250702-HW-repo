userinput = input("Expression: ")

x, y, z =  userinput.split(" ")
x = int(x)
z = int(z)

match y:
    case "+":
        print(f"{x+z:.1f}")
    case "-":
        print(f"{x-z:.1f}")
    case "*":
        print(f"{x*z:.1f}")
    case "/":
        print(f"{x/z:.1f}")
    case _:
        exit()