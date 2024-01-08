def main():
    time = input("What time is it? ").lower()
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    # Deciding if we need to add 12 to hours (1 a.m. = 1 + 12 = 13:00)
    if "p.m." in time:
        n = 12
    else:
        n = 0

    # Remove "a.m." or "p.m." and spaces
    time = time.replace("a.m.", "").replace("p.m.", "").strip()

    # Split time to hours and minutes
    h, m = map(float, time.split(":"))

    # Make sure time will be correct if "p.m." format is used
    h += n

    # e.g. 30 minutes - 0.5
    m /= 60

    return h + m



if __name__ == "__main__":
    main()