from datetime import date, timedelta
import sys

sequence = ("", "thousand", "million", "billion", "trillion")
digit_format = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
digit_format1 = ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
digit_format2 = ("", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")

def is_digit(s: str, length: int = 1) -> bool:
    if len(s) != length:
        return False
    for i in s:
        try:
            int(i)
        except:
            return False
    return True

def extract_input(userinput: str) -> tuple[int, int, int] | None:
    if userinput.count("-") != 2:
        return 
    y, m, d = userinput.split("-")
    if not is_digit(y, 4) or not is_digit(m, 2) or not is_digit(d, 2):
        return 
    return int(y), int(m), int(d)

def _format_two_digit_num(num: str) -> str:
    if num[0] == "1":
        return digit_format1[int(num[1])]
    if num[1] == "0":
        return digit_format2[int(num[0])]
    if num[0] == "0":
        return digit_format[int(num)]
    return f"{digit_format2[int(num[0])]}-{digit_format[int(num[1])]}"

def _format_num(num: str) -> str:
    num = str(int(num))
    num_len = len(num)
    result = ""
    if num_len == 3:
        if num[1] == "0" and num[2] == "0":
            result = f"{digit_format[int(num[0])]} hundred"
        else:
            result = f"{digit_format[int(num[0])]} hundred {_format_two_digit_num(num[1:])}"
    elif num_len == 2:
        result = _format_two_digit_num(num)
    elif num_len == 1:
        result = digit_format[int(num[0])]
    return result

def format_deltatime(deltatime: timedelta) -> str:
    output = ""
    minutes = str(round(deltatime.total_seconds() / 60))
    if minutes == "1":
        return "One minute"
    count = 0
    r = len(minutes) // 3 - 1 if len(minutes) % 3 == 0 else len(minutes) // 3
    for _ in range(r):
        substr = minutes[-3:]
        minutes = minutes[:-3]
        if substr != "000":
            if count == 0:
                output = f"{_format_num(substr).strip()} {sequence[count]}"
            else:
                output = f"{_format_num(substr).strip()} {sequence[count]}, {output.strip()}"
        count += 1
    if count == 0:
        output = f"{_format_num(minutes).strip()} {sequence[count]}"
    else:
        output = f"{_format_num(minutes).strip()} {sequence[count]}, {output.strip()}"
    output = " ".join((output[0].upper() + output[1:].strip(),  "minutes"))
    return output

def main() -> None:
    userinput = input("Date of Birth: ")
    result = extract_input(userinput)
    if result is None:
        print("Invalid date")
        sys.exit(1)
    y, m, d = result
    try:
        birthdate = date(y, m, d)
    except:
        print("Invalid date")
        sys.exit(1)
    nowtime = date.today()
    if birthdate > nowtime:
        print("Invalid date")
        sys.exit(1)
    deltatime = nowtime - birthdate
    output = format_deltatime(deltatime)
    print(output)

if __name__ == "__main__":
    main()