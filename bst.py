from dataclasses import dataclass


class treeNode:
   def __init__(self,data):
       self.data=data
       self.leftchild=None
       self.rightchild=None

newBT=treeNode("drink")
leftchild=treeNode("hot")
rightchild=treeNode("cold")
tea=treeNode("tea")
cofiee=treeNode("cofiee")
leftchild.leftchild=treeNode(" tea")
leftchild.rightchild=treeNode("cofiee")
alcoholic=treeNode("alcoholic")
nonalcoholic=treeNode("nonalcoholic")
rightchild.rightchild=treeNode("nonalcoholic")
rightchild.leftchild=treeNode("alcohlic")
newBT.leftchild=leftchild
newBT.rightchild=rightchild


def preordertraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preordertraversal(rootnode.leftchild)
    preordertraversal(rootnode.rightchild)

preordertraversal(newBT)
print("output of preordertraversal of binaray serch tree!!!")


def inordertraversal(rootnode):
    if not rootnode:
        return
    inordertraversal(rootnode.leftchild)
    print(rootnode.data)
    inordertraversal(rootnode.rightchild)

inordertraversal(newBT)
print("output of inordertraversal of binaray serch tree!!!")

def postordertraversal(rootnode):
    if not rootnode:
        return
    postordertraversal(rootnode.leftchild)
    postordertraversal(rootnode.rightchild)
    print(rootnode.data) 

postordertraversal(newBT)
print("output of postordertraversal of binaray serch tree!!!")
     
    