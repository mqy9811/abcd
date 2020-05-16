import multiprocessing
import _thread
import time


def work1(thread_name, sleep_time):
    print("线程名：", thread_name)
    time.sleep(sleep_time)
    print("{} 线程结束".format(thread_name))


def work2(thread_name, sleep_time):
    print("线程名：", thread_name)
    time.sleep(sleep_time)
    print("{} 线程结束".format(thread_name))


if __name__ == "__main__":
    print("main process starts",end="\n----------------------\n")
    _thread.start_new_thread(work1, ('thread01', 3))
    _thread.start_new_thread(work2, ('thread02', 2))
    time.sleep(6)