import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

# Check command-line arguments
if len(sys.argv) == 1:
    # Zero arguments: random font
    font = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] not in ['-f', '--font'] or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    font = sys.argv[2]
else:
    sys.exit("Invalid usage")

figlet.setFont(font=font)
text = input("Input: ")
print("Output:\n", figlet.renderText(text))
