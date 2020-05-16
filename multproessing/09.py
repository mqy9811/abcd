import threading
import time


def fun1(thread_name, sleep_time):
    print("{} 线程调用了 fun1".format(thread_name))
    time.sleep(sleep_time)
    print("1-结束", end="\n")


def fun2(thread_name, sleep_time):
    print("{} 线程调用了 fun1".format(thread_name))
    time.sleep(sleep_time)
    print("2-结束", end="\n")


if __name__ == "__main__":
    thread1 = threading.Thread(target=fun1, args=("thread-1", 3))
    thread2 = threading.Thread(target=fun2, args=("thread-2", 3))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()