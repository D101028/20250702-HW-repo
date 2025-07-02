def main():
    userinput = input("Input: ")
    print("Output:", shorten(userinput))


def shorten(word: str):
    result = ""
    for c in word:
        if c.lower() not in "aeiou":
            result += c
    return result


if __name__ == "__main__":
    main()
