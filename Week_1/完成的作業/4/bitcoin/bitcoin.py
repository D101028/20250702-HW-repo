import json
import requests
import sys

def format_price(price: float):
    s = f"{price:.4f}"
    i, j = s.split(".")
    i = "{:,}".format(int(i))
    return f"${i}.{j}"

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    num = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

try:
    # url = "https://api.coincap.io/v2/assets/bitcoin"
    # data = json.loads(requests.get(url).text)
    # price = float(data["data"]["priceUsd"])
    price = 97845.0243
    print(format_price(price * num))
except requests.RequestException:
    sys.exit()
