price = 50
accepted_den = [25, 10, 5]

while price > 0:
    # Print missing amount and ask for input
    print(f"Amount Due: {price}")
    coin = int(input("Insert Coin: "))

    # If coin is accepted denomination - substract it from the price
    if coin in accepted_den:
        price -= coin

# Print change
print(f"Change Owed: {price * -1}")