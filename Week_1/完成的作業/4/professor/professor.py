import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        for _ in range(3):
            userinput = input(f"{a} + {b} = ")
            try:
                userinput = int(userinput)
                if userinput != a + b:
                    print("EEE")
                    continue
                else:
                    score += 1
                    break
            except:
                continue
        else:
            print(f"{a} + {b} = {a+b}")
    print("Score:", score)

def get_level() -> int:
    userinput = input("Level: ")
    if userinput not in "123":
        return get_level()
    else:
        return int(userinput)


def generate_integer(level: int):
    lower = 10 ** (level - 1) if level != 1 else 0
    upper = 10 ** level - 1
    return random.randint(lower, upper)


if __name__ == "__main__":
    main()