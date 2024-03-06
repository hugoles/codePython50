import requests
import sys

try:
    n = sys.argv[1]
    bitcoin = float(n)
except ValueError:
    print("Error: Invalid number of Bitcoins specified.")
    sys.exit(1)
except IndexError:
    print("Error: Missing command-line argument.")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    rate = data["bpi"]["USD"]["rate_float"]
except requests.RequestException as e:
    print(f"Error: Unable to fetch Bitcoin price from the API. {e}")
    sys.exit(1)

amount = bitcoin * rate
print(f"${amount:,.4f}")

