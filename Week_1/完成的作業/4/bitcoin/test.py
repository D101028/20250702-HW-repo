def format_price(price: float):
    s = f"{price:.4f}"
    i, j = s.split(".")
    i = "{:,}".format(int(i))
    return f"{i}.{j}"

print(format_price(114514.1919810))
