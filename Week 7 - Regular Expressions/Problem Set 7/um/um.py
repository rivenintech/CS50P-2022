import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    result = re.findall(r"\bum\b", s, flags=re.IGNORECASE)

    return len(result)


if __name__ == "__main__":
    main()
