def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    number_started = False
    for _, c in enumerate(s):
        if not c.isalnum():
            return False

        if c.isdigit():
            if not number_started:
                number_started = True
                if c == '0':
                    return False 
        
        elif number_started:
            return False

    return True


if __name__ == "__main__":
    main()
