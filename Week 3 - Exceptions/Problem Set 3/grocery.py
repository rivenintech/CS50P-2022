groceries = {}

# Getting input until user stops it with CTRL+D
while True:
    try:
        item = input().upper()
    except EOFError:
        print()  # Print new line

        # Print all groceries (sorted alphabetically)
        for i in sorted(groceries):
            print(f"{groceries[i]} {i}")

        # Exit from program
        exit()

    # If item exists increment amount else add to dict
    if item in groceries:
        groceries[item] += 1
    else:
        groceries[item] = 1
