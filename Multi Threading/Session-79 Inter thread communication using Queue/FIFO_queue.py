import queue
q=queue.Queue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
q.put(0)
while not q.empty():
    print(q.get(),end=' ')
    
print()

q=queue.Queue()
q.put((5,'Aditya'))
q.put((3,'Shreeram'))
q.put((2,'Aniketh'))
q.put((1,'Sudrashan'))
q.put((4,'Rana'))
while not q.empty():
    print(q.get()[1],end=' ') 
