text = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

# Check if user's input is one of the correct answers
if text in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("No")