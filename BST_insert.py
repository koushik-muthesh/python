class Node:

     def __init__(self,data):
         self.data=data
         self.right=None
         self.left=None

def insert(node,data):
    if node is None:
        return Node(data)

    if data<node.data:
        node.left=insert(node.left,data)

    else:
        node.right=insert(node.right,data)

    return node


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root=None
n=int(input())
for i in range(n):
    a=int(input())
    root=insert(root,a)


inorder(root)
                            
