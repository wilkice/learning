def gen(num):
    a = 0
    b =1
    index = 0
    while index < num: # while not if
        yield a
        a, b = b, a+b
        index +=1

f = gen(10)
try:
    while True:
        i = next(f)
        print(i)
except StopIteration:
    print('out of index')


