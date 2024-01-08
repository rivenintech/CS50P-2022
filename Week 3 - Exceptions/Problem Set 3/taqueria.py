items = {  # Dict of items
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

cost = 0  # Total cost of items

# Getting input until it's correct
while True:
    # Check if user wants to continue ordering
    try:
        item = input("Item: ").title()
    except EOFError:
        print()
        break

    # Check if user's value is correct
    try:
        cost += items[item]
    except KeyError:
        continue

    # Print total cost
    print(f"Total: ${cost:.2f}")
