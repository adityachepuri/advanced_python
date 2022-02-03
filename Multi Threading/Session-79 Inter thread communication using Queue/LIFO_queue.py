import queue
q=queue.LifoQueue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
q.put(0)
while not q.empty():
    print(q.get(),end=' ') 
