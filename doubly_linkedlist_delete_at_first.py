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
            new_node.prev=cur

    def display(self):
        if self.head==None:
            print('list is empty')
            return
        cur=self.head
        while(cur.next!=None):
            print(cur.data)
            cur=cur.next
        print(cur.data)
    
    def delete_at_first(self):
        if self.head==None:
            print('list is empty nothing to delete')
            return
        else:
            self.head=self.head.next
            self.prev=None

llist=Doubly_linkedlist()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
llist.insert_at_end(80)
print('linked list after inserting elements')
llist.display()
print('linked list after deleting first element')
llist.delete_at_first()
llist.display()
print('linked list after deleting second element')
llist.delete_at_first()
llist.display()
print('linked list after deleting third element')
llist.delete_at_first()
llist.display()
print('linked list after deleting fourth element')
llist.delete_at_first()
llist.display()

