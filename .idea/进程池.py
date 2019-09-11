import multiprocessing
import time
def fun(msg):
    print("开始子进程：",msg)
    time.sleep(2)
    print("结束子进程：",msg)

if __name__=='__main__':
    pool = multiprocessing.Pool(3)
    for i in range(1,6):
        msg='进程%d'%i
        pool.apply_async(fun,(msg,))#非阻塞写入阻塞写入是apply

    pool.close()
    pool.join()
