import sys, requests

# Get how much BTC user would like to buy
try:
    amount = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

# Get current bitcoin price
try:
    resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    sys.exit("Something went wrong with API call")

# Calculate price for user's BTC and print it
btc_price = resp["bpi"]["USD"]["rate_float"] * amount
print(f"${btc_price:,.4f}")
