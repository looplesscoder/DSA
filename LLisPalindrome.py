#O(N)-TC 
#O(1)- SC
#BruteForce- O(N)-SC by storing the ele of ll in array and then checking isPalindrome

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
def insertNode(head, val):
    newNode= Node(val)
    if head is None:
        head=newNode
        return head 
    
    #going to the end of ll 
    temp= head
    while temp.next!=None:
        temp= temp.next 
    newNode= temp.next 
    
    return head 

def reverse(head):
    prev=None 
    temp=None 
    
    curr=head 
    while curr:
        #store the next node after current node in temp
        temp= curr.next 
        #make currs next point to dummy Node 
        curr.next= prev
        #now prev becomes curr 
        prev =curr 
        #curr becomes the next node 
        curr=temp 
    return prev 
    
def isPalindrome(head):
    if head== None or head.next==None:
        return True
    head1= head 
    slow,fast= head, head
    while fast.next!=None and fast.next.next!=None:
        slow= slow.next 
        fast= fast.next.next 
    head2= reverse(slow.next)
    
    while head2:
        if head1.data!= head2.data:
            return False 
        head1=head1.next
        head2=head2.next
    return True 
    
if __name__ == "__main__":
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 2)
    head = insertNode(head, 1)
    print(isPalindrome(head))
        
    
    
    