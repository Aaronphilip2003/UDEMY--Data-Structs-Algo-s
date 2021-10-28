class BinaryTree(object):
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
    
    def insertLeftChild(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    
    def insertRightChild(self,newNode):
        if self.rightChild == None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t
    
    def getRootVal(self):
        return self.key
    
    def setRootVal(self,obj):
        self.key=obj
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild

def preOrder(tree):
    if tree:
        print(tree.getRootVal())
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())

r=BinaryTree('1')
r.insertLeftChild('2')
r.insertRightChild('3')
preOrder(r)
# print(r.getRootVal())
# print(r.getLeftChild().getRootVal())
# print(r.getRightChild().getRootVal())