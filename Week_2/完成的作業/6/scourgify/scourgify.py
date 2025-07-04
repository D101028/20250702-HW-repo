import os
import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

_, f1, f2 = sys.argv

if not os.path.isfile(f1):
    sys.exit(f"Could not read {f1}")

with open(f1, mode="r", newline='') as infile, open(f2, mode="w", newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in reader:
        name = row["name"].strip('"')
        if ", " in name:
            last, first = name.split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})
