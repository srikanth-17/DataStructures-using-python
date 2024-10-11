class Tree:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data
    
    def insertn(self,data):
        if data < self.data:
            if self.left is None:
                self.left=Tree(data)
            else:
                self.left.insertn(data)
        else:
            if self.right is None:
                self.right=Tree(data)
            else:
                self.right.insertn(data)
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

    def find(self,x):
        if x< self.data:
            if self.left is None:
                return False
            else:
                return self.left.find(x)
        elif x> self.data:
            if self.right is None:
                return False
            else:
                return self.right.find(x)
        else:
            return True

              

tr=Tree(10)
tr.insertn(5)
tr.insertn(2)
tr.insertn(20)
tr.insertn(11)
tr.insertn(16)
tr.insertn(6)
print(tr.find(10))

