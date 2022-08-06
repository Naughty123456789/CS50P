class Jar:
    def __init__(self, capacity=12):
        self._capacity= capacity
        self._size=0

        if self._capacity<0:
            raise ValueError("Wrong capacity")


    def __str__(self):
        return self._size * "🍪"



    def deposit(self, n):
        if n + self._size <= self._capacity:
            self._size+=n
        else:
            raise ValueError("Too much")


    def withdraw(self, n):
        if n< self._size:
            self._size-=n
        else:
            raise ValueError("Not enough")



    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
       return self._size


jar=Jar()
jar.deposit(8)
jar.withdraw(4)
print(jar)