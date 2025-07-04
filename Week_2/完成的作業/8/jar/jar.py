class Jar:
    def __init__(self, capacity: int = 12):
        if not isinstance(capacity, int) or capacity < 0: # type: ignore
            raise ValueError("Invalid capacity")

        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n: int):
        if n > self.capacity - self.size:
            raise ValueError("Out of capacity")
        self.size += n

    def withdraw(self, n: int):
        if n > self.size:
            raise ValueError("Out of size")
        self.size -= n
