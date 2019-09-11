from multiprocessing import Queue
q = Queue(3)
q.put("消息1")
q.put("消息2")
q.put("消息3")
print(q.qsize())
print("当前队列是否已满",q.full())
if not q.full():
    q.put("消息4",block=True,timeout=1)
if not q.empty():
    print(q.get(block=True,timeout=1))
for i in range(q.qsize()):
    print(q.get())