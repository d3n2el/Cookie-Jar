class Jar:
    def __init__(self, capacity=12):
        self._size= 0
        if capacity < 0:
            raise ValueError("Not enough cookies")
        self.capacity = capacity

    def __str__(self):


    def deposit(self, n):
        self._size =  self._size+ n
        if self._size > 12:
            raise ValueError("Too many cookies")

    def withdraw(self, n):
        self._size=  self._size - n
        if self._size < 0:
            raise ValueError("Cookies cant be negative")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size