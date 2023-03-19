#done using stack 
# TC- O(N)
# SC- O(N)

class Node:
    def __init__(self,data):
        self.data= data 
        self.left= None 
        self.right=None 

def mirrorify(root):
    stack=[]
    stack.append(root)
    while stack!=None:
        root= stack.pop()
        if root is not None:
            stack.append(root.left)
            stack.append(root.right)
            root.left, root.right= root.right, root.left 
    
def inorder(root):
    inorder(root.left)
    print(root.data, end="")
    inorder(root.right)      
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    mirrorify(root)
    print("inorder traversal is ")
    inorder(root)