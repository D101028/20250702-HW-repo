import os
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

if not os.path.isfile(filename):
    sys.exit("File does not exist")

with open(filename, mode='r') as fp:
    lines = fp.read().split("\n")
    line = lines[0].strip()
    a, b, c = line.split(",")
    num = len(a) + 3
    a = a + " " * 3
    b = b + "   "
    c = c + "   "
    print(f"+-{'-' * num}+---------+---------+")
    print(f"| {a}| {b}| {c}|")
    print(f"+={'=' * num}+=========+=========+")
    for line in lines[1:]:
        if line.strip() == "":
            continue
        a, b, c = line.split(",")
        a = a + " " * (num-len(a))
        b = b + "  "
        c = c + "  "
        print(f"| {a}| {b}| {c}|")
        print(f"+-{'-' * num}+---------+---------+")
