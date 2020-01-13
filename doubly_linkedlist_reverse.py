class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Doubly_linkedlist:

    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
        if self.head==None:
            new_node=Node(data)
            self.head=new_node
            return
        cur=self.head
        new_node=Node(data)
        while(cur.next!=None):
            cur=cur.next
        cur.next=new_node
        cur.prev=None

    def display(self):
        if self.head==None:
            print('list is empty')
            return
        cur=self.head
        while(cur.next!=None):
            print(cur.data)
            cur=cur.next
        print(cur.data)
    
    def reverse(self):
        if self.head==None:
            print('list is empty')
            return
        p=self.head
        q=p.next
        p.next=None
        p.prev=q
        while q!=None:
            q.prev=q.next
            q.next=p
            p=q
            q=q.prev
        self.head=p

llist=Doubly_linkedlist()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
llist.insert_at_end(80)
print('linked list before reversing')
llist.display()
print('linked list after reversing')
llist.reverse()
llist.display()
