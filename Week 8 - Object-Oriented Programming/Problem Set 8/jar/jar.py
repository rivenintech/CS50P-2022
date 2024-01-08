class Jar:
    def __init__(self, capacity=12):
        # Check if capacity is non-negative int
        if int(capacity) < 0:
            raise ValueError("Invalid capacity")

        self._capacity = int(capacity)
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        # Check if cookies will fit into a jar
        if self.cookies + n > self._capacity:
            raise ValueError("Too many cookies")

        self.cookies += n

    def withdraw(self, n):
        # Check if there is enough cookies to eat
        if self.cookies - n < 0:
            raise ValueError("There's not enough cookies to eat")

        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
