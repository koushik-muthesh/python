class BST:
    def __init__(self,data):
        self.key=data
        self.right=None
        self.left=None

def insert(node,data):
    if node is None:
        return BST(data)
    
    if node.key>data:
        node.left=insert(node.left,data)
    else:
        node.right=insert(node.right,data)

    return node

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
        

root=None
n=int(input())
for i in range(n):
    root=insert(root,int(input()))

inorder(root)
