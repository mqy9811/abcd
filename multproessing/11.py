from threading import Thread, Lock
NUM = 0
lock = Lock()


def func1():
    global NUM
    for i in range(10000000):
        lock.acquire()
        NUM += 1
        lock.release()
    print("func1 的NUM：", NUM)


def func2():
    global NUM
    for i in range(10000000):
        lock.acquire()
        NUM += 1
        lock.release()
    print("func2 的NUM：", NUM)


if __name__ == "__main__":
    print("main process starts")
    thread1 = Thread(target=func1)
    thread2 = Thread(target=func2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("end")