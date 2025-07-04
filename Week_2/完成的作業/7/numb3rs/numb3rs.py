
def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip: str):
    if ip.count(".") != 3:
        return False

    arr = ip.split(".")
    for i in arr:
        if i.startswith("0") and i.replace("0", "") != "":
            return False
    try:
        arr = list(map(int, arr))
    except:
        return False

    if not all(0 <= i <= 255 for i in arr):
        return False

    return True

if __name__ == "__main__":
    main()

