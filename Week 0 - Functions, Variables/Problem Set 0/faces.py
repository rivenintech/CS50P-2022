def main():
    text = input()
    print(convert(text))


def convert(text: str):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    return text


main()