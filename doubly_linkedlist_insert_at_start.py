class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Doubly_linkedlist:
    
    def __init__(self):
        self.head=None

    def insert_at_start(self,data):
        if self.head==None:
            new_node=Node(data)
            self.head=new_node
            return
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        cur=self.head
        while(cur.next!=None):
            print(cur.data)
            cur=cur.next
        print(cur.data)

llist=Doubly_linkedlist()
llist.insert_at_start(10)
llist.insert_at_start(20)
llist.insert_at_start(30)
llist.insert_at_start(40)
llist.insert_at_start(50)
llist.insert_at_start(60)
llist.insert_at_start(70)
llist.display()
