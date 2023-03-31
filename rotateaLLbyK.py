class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
def insertNode(head, val):
    newNode= Node(val)
    
    if head is None:
        head= newNode 
        return head 
    #going to the end of ll
    temp= head
    while temp.next!=None:
        temp=temp.next 
    temp.next= newNode 
    newNode.next=None 
    
    return head 
    
        
def rotateLL(head, k):
    #check if there is 1 node or no node 
    if head is None or head.next is None:
        return head 
    
    for i in range(k):
        #reaching end of the list whilst storing its previous and end node 
        curr= head 
        while curr.next.next!= None:
            curr=curr.next 
        #curr is prev 
        #end is curr.next 
        end= curr.next
        curr.next= None
        end.next=head 
        head= end 
        
    return head 
    
def printList(head):
    temp=head 
    while temp!=None:
        print(temp.val, '-->')
        temp=temp.next 
    return 

if __name__ == '__main__':
    head = None
    # inserting Node
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)


    print("Original list: ", end='')
    printList(head)


    k = 2
    # calling function for rotating right of the nodes by k times
    newHead = rotateLL(head, k)


    print("After", k, "iterations: ", end='')
    printList(newHead)  # list a