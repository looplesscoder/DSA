class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
# Returns true if there is a path from
# root to the given node. It also
# populates 'arr' with the given path
def hasPath(root, arr, x):
     
    # if root is None there is no path
    if (not root):
        return False
     
    # push the node's value in 'arr'
    arr.append(root.data)    
     
    # if it is the required node
    # return true
    if (root.data == x):    
        return True
     
    # else check whether the required node
    # lies in the left subtree or right
    # subtree of the current node
    if (hasPath(root.left, arr, x) or
        hasPath(root.right, arr, x)):
        return True
     
    # required node does not lie either in
    # the left or right subtree of the current
    # node. Thus, remove current node's value 
    # from 'arr'and then return false    
    arr.pop(-1)
    return False
 
# function to print the path from root to
# the given node if the node lies in
# the binary tree
def printPath(root, x):
     
    # vector to store the path
    arr = []
     
    # if required node 'x' is present
    # then print the path
    if (hasPath(root, arr, x)):
        for i in range(len(arr) - 1):
            print(arr[i], end = "->")
        print(arr[len(arr) - 1])
     
    # 'x' is not present in the
    # binary tree
    else:
        print("No Path")
 
# Driver Code
if __name__ == '__main__':
     
    # binary tree formation
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
         
    x = 5
    printPath(root, x)
     