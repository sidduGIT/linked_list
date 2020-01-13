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
        new_node.prev=cur
        
    def insert_after_value(self,after,data):
        if self.head==None:
            print('list is empty')
            return
        cur=self.head
        while(cur.next!=None):
            if cur.data==after:
                break
            cur=cur.next
        if cur.next==None:
            print(after,'item not found in the list')
        else:
            new_node=Node(data)
            new_node.prev=cur
            new_node.next=cur.next
            #if cur.next!=None:
            #    cur.next.prev=new_node
            cur.next=new_node

    def display(self):
        cur=self.head
        while(cur.next!=None):
            print(cur.data)
            cur=cur.next
        print(cur.data)

llist=Doubly_linkedlist()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
print('doubly linkedlist after inserting at end')
llist.display()
llist.insert_after_value(20,500)
llist.insert_after_value(60,600)
llist.insert_after_value(40,700)
print('doubly linkedlist after inserting at after value')
llist.display()
