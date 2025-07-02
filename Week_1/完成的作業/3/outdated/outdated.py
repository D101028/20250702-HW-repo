arr = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        userinput = input("Date: ")
        if "/" in userinput:
            m, d, y = map(int, userinput.split("/"))
            print(f"{y:04}-{m:02}-{d:02}")
        else:
            data = userinput.split(", ")
            assert len(data) == 2
            y = int(data[1])
            m, d = data[0].split()
            m = arr.index(m) + 1
            d = int(d)
            print(f"{y:04}-{m:02}-{d:02}")
        break
    except:
        continue
