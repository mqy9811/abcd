from multiprocessing import *
import time


def write(q):
    a = ["a", "b", "c", "d", "e"]
    for i in a:
        print("写入信息：{}".format(i))
        q.put(i)
        time.sleep(1)


def read(q):
    for i in range(q.qsize()):
        message = q.get()
        print("读取信息：{}".format(message))
        time.sleep(1)


if __name__ == "__main__":
    q = Manager().Queue()
    pool = Pool(3)
    pool.apply(func=write, args=(q,))
    pool.apply(func=read, args=(q, ))
    pool.close()

