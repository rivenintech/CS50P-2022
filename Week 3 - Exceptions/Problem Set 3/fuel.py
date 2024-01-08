# Getting input until it's correct
while True:
    try:
        x, y = map(int, input("What's the fuel level? (X/Y) ").split("/"))
    except ValueError:
        continue

    if x <= y and y != 0:
        break

# Calculating percentage
perc = x / y * 100

# Print correct output
if perc >= 99:
    print("F")
elif perc <= 1:
    print("E")
else:
    print(f"{round(perc)}%")
