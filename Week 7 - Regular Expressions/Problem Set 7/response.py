import validators

if validators.email(input("What's your email addres? ")):
    print("Valid")
else:
    print("Invalid")
