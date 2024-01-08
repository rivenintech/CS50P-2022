text = input("camelCase: ")

# Loop through all letters in string
for letter in text:
    # If letter is uppercase - print "_" and make it lowercase
    if letter.isupper():
        print("_", end="")
        letter = letter.lower()

    print(letter, end="")

print()