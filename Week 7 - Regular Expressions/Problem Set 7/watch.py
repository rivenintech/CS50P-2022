import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'src="https?://(?:www.)?youtube\.com/embed/(\w+?)"'

    # If pattern is matching - extract video id and format it as new URL
    if result := re.search(pattern, s):
        return f"https://youtu.be/{result.group(1)}"

    return None


if __name__ == "__main__":
    main()
