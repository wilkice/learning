from collections import Iterable
from collections import Iterator

class Fibonacci():
    def __init__(self, num):
        self.num =num
        self.a = 0
        self.b = 1
        self.index = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.index < self.num:
            result = self.a
            self.a, self.b = self.b , self.a + self.b
            self.index +=1
            return result
        else:
            raise StopIteration


f =Fibonacci(15)
try:
    for i in f:
        print(i)
except StopIteration:
    raise
    # print('out of index')

