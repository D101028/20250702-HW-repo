import os
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

if not os.path.isfile(filename):
    sys.exit("File does not exist")

total = 0

with open(filename, mode="r") as fp:
    lines = fp.read().split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        total += 1

print(total)
