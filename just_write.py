import multiprocessing

def run():
    for i in range(5):
        print('hi', i)

if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    for i in range(10):
        pool.apply_async(run)
    pool.close()
    pool.join()