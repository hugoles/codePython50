class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError
        self.Ccapacity = capacity
        self.Csize = 0

    def __str__(self):
        return '🍪' * self.Csize

    def deposit(self, n):
        if self.Csize + n > self.Ccapacity or not isinstance(n, int):
            raise ValueError
        self.Csize += n

    def withdraw(self, n):
        if self.Csize - n < 0 or not isinstance(n, int):
            raise ValueError
        self.Csize -= n

    @property
    def capacity(self):
        return self.Ccapacity

    @property
    def size(self):
        return self.Csize
