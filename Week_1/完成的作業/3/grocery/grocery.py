result: dict[str, int] = {}
while True:
    try:
        item = input().upper()
        if result.get(item) is None:
            result[item] = 1
        else:
            result[item] += 1
    except EOFError:
        print()
        break

for item in sorted(result.keys()):
    print(f"{result[item]} {item}")
