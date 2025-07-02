def main():
    userinput = input("What time is it? ")
    h = convert(userinput)
    if 7 <= h <= 8:
        print("breakfast time")
    elif 12 <= h <= 13:
        print("lunch time")
    elif 18 <= h <= 19:
        print("dinner time")

def convert(time: str) -> float:
    h, m = map(int, time.split(":"))
    h = h + m / 60
    return h

if __name__ == "__main__":
    main()