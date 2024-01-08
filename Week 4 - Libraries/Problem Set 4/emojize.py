from emoji import emojize

# Get input from user and output "emojized" version
text = input("Input: ")
print(f"Output: {emojize(text, language='alias')}")
