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
    print("main process starts")
    q = Queue()
    qw = Process(target=write, args=(q,))
    qr = Process(target=read, args=(q,))
    qw.start()
    qw.join()
    qr.start()
    qr.join()
    print("main process ends")
