# coding=utf-8
import multiprocessing
import time


def child(message, interval):
    print("{} is start".format(message))
    time.sleep(interval)
    print("{} is over".format(message))


if __name__ == "__main__":
    print("main process starts")
    pool = multiprocessing.Pool(3)
    for i in range(5):
        message = "mission {}".format(i)
        pool.apply_async(func=child, args=(message, 3))
    pool.close()
    pool.join()

    print("main process is over!")
