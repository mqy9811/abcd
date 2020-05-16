import threading
import time

def fun1(delay):
    print("现在运行的是线程--{}".format(threading.current_thread().getName()))
    time.sleep(delay)
    print("线程：{} 运行结束".format(threading.current_thread().getName()))


def fun2(delay):
    print("现在运行的是线程--{}".format(threading.current_thread().getName()))
    time.sleep(delay)
    print("线程：{} 运行结束".format(threading.current_thread().getName()))


class MyThread(threading.Thread):
    def __init__(self, func, name, args):
        super().__init__(self, target=func, name=name, args=args)

    def run(self):
        self._target(*self.args)


if __name__ == "__main__":
    thread1 = MyThread(fun1, "thread01", (2,))
    thread2 = MyThread(fun2, "thread02", (3,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()