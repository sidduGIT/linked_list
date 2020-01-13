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
        else:
            cur=self.head
            new_node=Node(data)
            while(cur.next!=None):
                cur=cur.next
            cur.next=new_node
            cur.prev=None

    def display(self):
        if self.head==None:
            print('list is empty')
        cur=self.head
        while(cur.next!=None):
            print(cur.data)
            cur=cur.next
        print(cur.data)

    def delete_at_end(self):
        if self.head==None:
            print('list is empty')
            return
        elif self.head.next==None:
            self.head=None
            return
        else:
            cur=self.head
            while(cur.next.next!=None):
                cur=cur.next
            cur.next=None


llist=Doubly_linkedlist()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
llist.insert_at_end(80)
llist.insert_at_end(90)
print('linked list before deleting any items')
llist.display()
print('after deleting last element')
llist.delete_at_end()
llist.display()
print('after deleting last element')
llist.delete_at_end()
llist.display()
print('after deleting last element')
llist.delete_at_end()
llist.display()
print('after deleting last element')
llist.delete_at_end()
llist.display()

