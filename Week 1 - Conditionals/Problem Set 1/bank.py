greeting = input("Greeting: ").strip().lower()

# Check if greeting startswith "hello" or "h" and print reward
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")