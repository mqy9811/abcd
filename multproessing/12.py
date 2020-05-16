import threading

local = threading.local()


def process_student():
    name = local.name
    print("student's name :%s" % name)
    print("this thread's name :{}".format(threading.current_thread().getName()))


def process_start(name):
    local.name = name
    process_student()


t1 = threading.Thread(target=process_start, args=("孟",))
t2 = threading.Thread(target=process_start, args=("张",))
t1.start()
t2.start()
t1.join()
t2.join()
