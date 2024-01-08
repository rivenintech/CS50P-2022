from random import randint


def main():
    level = get_positive_int("Level: ")
    num = randint(1, level)  # Generate random number

    while True:
        guess = get_positive_int("Guess: ")

        # Check if user guessed the number or if it's too high/low
        if guess == num:
            print("Just right!")
            break
        elif guess > num:
            print("Too large!")
        else:
            print("Too small!")


def get_positive_int(text):
    # Prompt user until the input is valid
    while True:
        try:
            n = int(input(text))
        except ValueError:
            continue

        # Check if it's a positive integer
        if n > 0:
            return n


if __name__ == "__main__":
    main()
