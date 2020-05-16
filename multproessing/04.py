# coding=utf-8

from multiprocessing import Process
import time
Num = 10


def work01():
    global Num
    Num += 10
    time.sleep(2)
    print("work 01 de Num:{}".format(Num))


def work02():
    global Num
    Num += 20
    time.sleep(2)
    print("work 02 de Num:{}".format(Num))

if __name__ == "__main__":
    print("main process's Num: {}".format(Num))
    p1 = Process(target=work01)
    p2 = Process(target=work02)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("the end's Num: {}".format(Num))