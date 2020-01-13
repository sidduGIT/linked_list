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
        else:
            cur=self.head
            while(cur.next!=None):
                print(cur.data)
                cur=cur.next
            print(cur.data)

    def delete_by_value(self,value):
        
        if self.head==None:
            print('list is empty no need to delete anything')
            return
        if self.head.next==None:
            if self.head.data==value:
                self.head=None
            else:
                print('item not found')
            return
        if self.head.data==value:
            self.head=self.head.next
            self.head.prev=None
            return
        
        cur=self.head
        while(cur.next!=None):
            if cur.data==value:
                break
            cur=cur.next
        if cur.next!=None:
            cur.prev.next=cur.next
            cur.next.prev=cur.prev
        else:
            if cur.data==value:
                cur.pre.next=None
            else:
                print('item not found')

llist=Doubly_linkedlist()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
llist.insert_at_end(80)
print('linked list after adding elements at end')
llist.display()
print('list after deleting 30')
llist.delete_by_value(30)
llist.display()
print('list after deleting 50')
llist.delete_by_value(50)
llist.display()
print('list after deleting 70')
llist.delete_by_value(70)
llist.display()
