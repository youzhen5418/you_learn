import threading
# 定义线程局部变量
mydata = threading.local()
# 定义准备作为线程执行体使用的函数
def action (max):
    for i in range(max):
        try:
            mydata.x += i
        except:
            mydata.x = i
        # 访问mydata的x的值
        print('%s mydata.x的值为: %d' %
            (threading.current_thread().name, mydata.x))
# 使用两个子线程
t1 = threading.Thread(target=action,args=(10,))
t2 = threading.Thread(target=action,args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()