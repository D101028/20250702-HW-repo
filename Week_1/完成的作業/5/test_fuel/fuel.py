def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction: str):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x < 0 or y <= 0:
            raise ValueError("X and Y must be positive integers.")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")
        return round(x / y * 100)
    except ZeroDivisionError:
        raise
    except Exception:
        raise ValueError("Invalid fraction format.")


def gauge(percentage: int):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
