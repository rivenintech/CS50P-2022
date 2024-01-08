vowels = ["a", "e", "i", "o", "u"]
text = input("Input: ")

# Loop through the string
for letter in text:
    # If letter is not a vowel - print it
    if not letter.lower() in vowels:
        print(letter, end="")

print()