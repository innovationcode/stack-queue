class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def printStack(self):
        for item in self.items:
            print(item, end = " -> ")


s1 = Stack()
print(s1.isEmpty())
print(s1.push(10))
print(s1.isEmpty())
print(s1.pop())
print(s1.isEmpty())
s1.push(20)
s1.push(40)
s1.push(60)
s1.push(80)
s1.printStack()
