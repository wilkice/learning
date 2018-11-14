from collections import Iterable
from collections import Iterator

class A():
    def __init__(self):
        self.list = []

    def myappend(self, item):
        self.list.append(item)


    def __iter__(self):
        ite = MyItrator(self.list)
        return ite


class MyItrator():
    def __init__(self, it_list):
        self.index = 0
        self.it_list = it_list

    def __iter__(self):
        return self


    def __next__(self):
        if self.index< len(self.it_list):
            self.index +=1
            return self.it_list[self.index-1]
        else:
            raise StopIteration


a = A()
a.myappend(2)
a.myappend(8)

# r = isinstance(a, Iterable)
# print(a)
# print(r)
for i in a:
    print(i)
