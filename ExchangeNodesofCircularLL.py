class Node:
    def __init__(self, data):
        self.data= data
        self.next= None 
def addToEmpty(head, data):
 
    # This function is only for empty list
    if (head != None):
        return head
 
    # Creating a node dynamically.
    temp = Node(data)
 
    # Assigning the data.
    temp.data = data
    head = temp
 
    # Creating the link.
    head.next = head
    return head
 
 
def addBegin(head, data):
 
    if (head == None):
        return addToEmpty(head, data)
 
    temp = Node(data)
    temp.data = data
    temp.next = head.next
    head.next = temp
 
    return head
 

def exchange(head):
    if head  is None or head.next==head:
        return head 
    
    elif head.next.next == head:
        head = head.next
        return head
    #assigning the head to a curr variable 
    curr= head 
    prev= curr
    #traverse the list 
    while curr.next!= head:
        prev= curr 
        curr=curr.next 
    
    prev.next= head
    temp= head.next
    head.next= curr
    curr.next=temp
    head= curr
    return head 
    
def traverse(head):
    if head==None:
        print("list is empty")
        return 
    
    temp= head 
    print(temp.data, end= "->")
    temp= temp.next 
    
    while temp!=head:
        print(temp.data, "->")
        temp= temp.next
        
if __name__ == '__main__':
 
    head = None
    head = addToEmpty(head, 6)
    for x in range(5, 0, -1):
        head = addBegin(head, x)
    print("List Before: ", end="")
    traverse(head)
    print()
 
    print("List After: ", end="")
    head = exchange(head)
    traverse(head)
    
        