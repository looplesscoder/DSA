#O(N)-TC , NAIVE APPROACH TC- O(2N)
#using slow and fast pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
 # 1 2 3 4 5
    # createNode and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
            
    def delete(self,head ,n):
        slow= head 
        fast= head 
        
        while n>0:
            fast= fast.next 
            n-=1 
        if fast.next==None:
            return headd.next 
        while fast.next!=None:
            slow= slow.next 
            fast=fast.next 
        slow.next= slow.next.next 
        return head 
        
if __name__ == '__main__':
    l = LinkedList()
    l.push(5)
    l.push(4)
    l.push(3)
    l.push(2)
    l.push(1)
    print('***** Linked List Before deletion *****')
    l.display()
 
    print('************** Delete nth Node from the End *****')
    l.delete(l.head, 2)
 
    print('*********** Linked List after Deletion *****')
    l.display()