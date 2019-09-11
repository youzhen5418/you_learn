import threading
from time import sleep
def fun1(threadname,delay):
    print("线程{}开始执行fun1".format(threadname))
    sleep(delay)
    print("线程{}结束执行fun1".format(threadname))

def fun2(threadname,delay):
    print("线程{}开始执行fun2".format(threadname))
    sleep(delay)
    print("线程{}结束执行fun2".format(threadname))


if __name__ =="__main__":
    print("开始执行")
    t1=threading.Thread(target=fun1,args=('thread-1',2))
    t2=threading.Thread(target=fun2,args=('thread-2',3))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

