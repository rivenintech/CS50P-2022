import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if result := re.search(r"^[1-9]\d{0,2}\.(?:\d{1,3}\.){2}[1-9]\d{0,2}$", ip):
        for part in ip.split("."):
            if int(part) > 255:
                break
        else:
            return True

    return False


if __name__ == "__main__":
    main()
