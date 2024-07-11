from multiprocessing.sharedctypes import Value
from optparse import Values
from re import X
from typing import ValuesView


class Queue:
    def __init__(self):
        self.item=[]

    def __str__(self):
        Values=[str(x) for x in self.item]
        return ' '.join(Values)

    def isEmpty (self):
        if self.item==[]:
            return True
        else:
            return False

    def enqueue(self,value):
        self.item.append(value)
        return "element inserted at the end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return "there is not elements in queue"
        else:
            return self.item.pop(0)

    def peek(self):
        if self.isEmpty():
            return "no elements in queue"
        else:
            return self.item[0]

    def delete(self):
        self.item=None

customQueue=Queue()
print(customQueue.isEmpty() ,"queue is empty")
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue , "elements inserted")
print(customQueue.dequeue(), "element deleted from first")
print(customQueue , "remaining element")
print(customQueue.peek(), " element peekup ")
print(customQueue.delete(), "queue is deleted")