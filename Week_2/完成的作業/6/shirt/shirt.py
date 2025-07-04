import os
import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

_, f1, f2 = sys.argv

if not any(f1.lower().endswith(i) for i in (".jpg",".jpeg",".png")) \
    and not any(f2.lower().endswith(i) for i in (".jpg",".jpeg",".png")):
    sys.exit("Input and output must be .jpg, .jpeg, or .png")

if f1.split(".")[-1] != f2.split(".")[-1]:
    sys.exit("Input and output have different extensions")

if not os.path.isfile(f1):
    sys.exit("Input does not exist")

input_image = Image.open(f1)
shirt = Image.open("shirt.png")

resized_image = ImageOps.fit(input_image, shirt.size)

resized_image.paste(shirt, mask=shirt)

resized_image.save(f2)

