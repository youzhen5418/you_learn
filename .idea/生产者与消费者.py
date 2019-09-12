from time import sleep
from threading import Thread
from queue import Queue

class Pruducter(Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize()<1000:
                for i in range(100):
                    msg = "生产第"+ str(count)+"个产品"
                    print(msg)
                    count += 1
                    queue.put(msg)
                sleep(0.5)

class Cusumer(Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize()>100:
                for i in range(10):
                    msg = self.name + "消费" + queue.get()
                    print(msg)
                sleep(1)

if __name__=="__main__":
    queue = Queue()
    p1 = Pruducter()
    c1 = Cusumer()
    p1.start()
    sleep(1)
    c1.start()
