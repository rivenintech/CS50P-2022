import random


def main():
    # Create score variable and get level
    score = 0
    level = get_level()

    # Create 10 math problems
    for _ in range(10):
        # Get random x, y and a sum of these values
        x = generate_integer(level)
        y = generate_integer(level)
        sum_xy = x + y

        # Check if user's answer is correct (they have 3 tries)
        for _ in range(3):
            try:
                answ = int(input(f"{x} + {y} = "))
            except ValueError:
                continue

            if answ == sum_xy:
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"{x} + {y} = {sum_xy}")

    print(f"Score: {score}")


def get_level():
    # Prompt user until they input number 1-3
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level in {1, 2, 3}:
            return level


# Generate random number with "n" digits
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)

    return random.randint(10 ** (level - 1), 10**level - 1)


if __name__ == "__main__":
    main()
