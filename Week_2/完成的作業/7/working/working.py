import re

def main():
    print(convert(input("Hours: ")))

def parse_time(time_str: str):
    match = re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM)", time_str)
    if not match:
        raise ValueError("Invalid time format")
    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    period = match.group(3)

    if hour < 1 or hour > 12 or minute < 0 or minute > 59:
        raise ValueError("Invalid time value")

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"

def convert(s: str):
    match = re.fullmatch(r"(.+) to (.+)", s)
    if not match:
        raise ValueError("Invalid input format")
    start, end = match.group(1).strip(), match.group(2).strip()
    start_24 = parse_time(start)
    end_24 = parse_time(end)
    return f"{start_24} to {end_24}"

if __name__ == "__main__":
    main()