import _thread
from time import sleep

def fuc1():
    print("开始运行fuc1")
    sleep(4)
    print("结束运行fuc1")
def fuc2():
    print("开始运行fuc2")
    sleep(5)
    print("结束运行fuc2")

if __name__ == "__main__":
    print("开始运行")
    _thread.start_new_thread(fuc1,())
    _thread.start_new_thread(fuc2,())
    sleep(7)