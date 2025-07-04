import re

def main():
    print(count(input("Text: ")))

def count(s: str):
    matches = re.findall(r"(?<![a-z])um(?![a-z])", s.lower())
    
    return len(matches)

if __name__ == "__main__":
    main()