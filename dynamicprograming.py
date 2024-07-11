class Node:
  def __init__(self,value=None):
        self.value=value
        self.next=None

class singleLinkedlist:                       
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def insert(self,value,location):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            if location ==0:
                newnode.next=self.head
                self.head=newnode
            elif location==1:
                newnode.next=None
                self.tail.next=newnode
                self.tail=newnode
            else:
                tempNode=self.head
                index=0
                while index < location-1:
                    tempNode=tempNode.next
                    index +=1
                nextnode=tempNode.next
                tempNode.next=newnode
                newnode.next=nextnode
                if tempNode==self.tail:
                    self.tail=newnode

singlelinkedlist=singleLinkedlist()
singlelinkedlist.insert(1,1)
singlelinkedlist.insert(2,1)
singlelinkedlist.insert(3,1)
singlelinkedlist.insert(4,1)
singlelinkedlist.insert(5,1)

print([node.value for node in singlelinkedlist])

        


      