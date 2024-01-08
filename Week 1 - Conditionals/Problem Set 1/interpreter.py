x, y, z = input("Expression: ").strip().split()

# Change variables to integers
x = float(x)
z = float(z)

# Print the expression result
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)