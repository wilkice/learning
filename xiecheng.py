import time
def work1():
    for i in range(3):
        print('work1: '+ str(i))
        yield


def work2():
    for i in range(5):
        print('work2: ' + str(i))
        yield

if __name__ == "__main__":
    w1= work1()
    w2 = work2()

    next(w1)
    next(w2)