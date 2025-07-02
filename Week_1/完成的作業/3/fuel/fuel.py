while True:
    try:
        userinput = input("Fraction: ")
        a = userinput.split("/")
        assert len(a) == 2
        x, y = map(float, a)
        assert int(x) == x and int(y) == y
        assert y != 0
        assert y >= x >= 0
        perc = round(x/y*100)
        if perc >= 99:
            print("F")
        elif perc <= 1:
            print("E")
        else:
            print(f"{perc}%")
        break
    except Exception as e:
        continue
