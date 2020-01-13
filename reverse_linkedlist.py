class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=new_node

    def display(self):
        if self.head==None:
            print('list is empty')
            return
        else:
            cur=self.head
            while cur.next!=None:
                print(cur.data)
                cur=cur.next
            print(cur.data)

    def reverse_linkedlist(self):
        prev=None
        cur=self.head
        while cur.next!=None:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        self.head=prev

llist=LinkedList()
print('initial list')
llist.display()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
llist.insert_at_end(80)
print('list after adding some elements')
llist.display()
print('list after reversing it')
llist.reverse_linkedlist()
llist.display()

    
