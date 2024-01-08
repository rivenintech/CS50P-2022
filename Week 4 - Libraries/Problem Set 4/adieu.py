import inflect

p = inflect.engine()
names = []

# Getting input until user stops it with CTRL+D
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

# Print names with commas and "and"
print(f"Adieu, adieu, to {p.join(names)}")
