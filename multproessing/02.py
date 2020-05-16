# coding=utf-8
from multiprocessing import Process
import time


class ClockProcess(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print("child process start, time:{}".format(time.ctime()))
        time.sleep(self.interval)
        print("child process is over, time:{}".format(time.ctime()))


if __name__ == "__main__":
    print("main process starts, time:{}".format(time.ctime()))
    P = ClockProcess(3)
    P.start()
    P.join()
    print("main process ends, time:{}".format(time.ctime()))
