CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMS = "0123456789"

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0] not in CHARS or s[1] not in CHARS:
        return False
    first_num = None
    for c in s[2:]:
        if c not in CHARS:
            if c in NUMS:
                if first_num is None:
                    if c == "0":
                        return False
                    first_num = c
            else:
                return False
        else:
            if first_num is not None:
                return False
    
    return True

main()