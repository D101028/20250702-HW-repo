import validators

def main():
    if check(input("What's your email address? ")):
        print("Valid")
    else:
        print("Invalid")

def check(s: str):
    return validators.email(s)

if __name__ == "__main__":
    main()
