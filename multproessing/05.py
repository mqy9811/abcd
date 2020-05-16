# coding=utf-8
from multiprocessing import Queue

q = Queue(3)

for i in range(5):
    if not q.full():
        q.put("message{}".format(i))
    else:
        print("q is full")
        break

for i in range(q.qsize()):
    print(q.get())
