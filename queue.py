class Queue(object):
    def __init__(self):
        self.items = []
        self.size1 = 0
    
    def enqueue(self, item):
        self.items.append(item)
        self.size1 += 1
    
    def dequeue(self):
        self.size1 -= 1
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return self.size1 
        #return len(self.items)
    
    def printqueue(self):
        for item in self.items:
            print(item, end = " -> ")

q = Queue()
q.enqueue(600)
print(q.isEmpty())
print(q.dequeue())
print(q.isEmpty())
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)
q.enqueue(500)
print("Size  : ",q.size())
q.printqueue()
print("\n",q.dequeue())

print(q.dequeue())

print(q.dequeue())




