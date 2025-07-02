arr: list[str] = []

def convert(arr: list[str]):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] + " and " + arr[1]
    result = ""
    for name in arr[:-1]:
        result += name + ", "
    result += "and " + arr[-1]
    return result

while True:
    try:
        name = input("Name: ")
        arr.append(name)
    except:
        print()
        break

print(f"Adieu, adieu, to {convert(arr)}")
