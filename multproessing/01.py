# coding=utf-8
from multiprocessing import Process
from time import sleep


def kid(name, age, interval):
    print("name:{0}  age:{1}".format(name, age))
    sleep(interval)
    print("all message has been shown")


if __name__ == "__main__":
    print("main process is running")
    p = Process(target=kid, args=("神", 22, 3))
    p.start()
    p.join()
    print("main process is over")
