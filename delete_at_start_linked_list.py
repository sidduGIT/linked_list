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
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def display(self):
        cur=self.head
        while cur.next!=None:
            print(cur.data)
            cur=cur.next
        print(cur.data)

    def delete_at_first(self):
        if self.head==None:
            print('list is empty')
            return
        else:
            self.head=self.head.next

llist=LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
print('after inserting items at the end')
llist.display()

print('after deleting first item')
llist.delete_at_first()
llist.display()

print('after deleting second item')
llist.delete_at_first()
llist.display()

print('after deleting third item')
llist.delete_at_first()
llist.display()


