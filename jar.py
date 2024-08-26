class Jar:
    def __init__(self, capacity=12):
        self._size= 0
        if capacity < 0:
            raise ValueError("Not enough cookies")
        self._capacity = capacity

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self._size+n > 12:
            raise ValueError("Too many cookies")
        self._size =  self._size+ n


    def withdraw(self, n):
        if self._size-n < 0:
            raise ValueError("Cookies cant be negative")
        self._size=  self._size - n
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
