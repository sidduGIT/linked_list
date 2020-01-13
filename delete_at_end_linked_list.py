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

    def delete_at_end(self):
        if self.head==None:
            print('list is empty')
        else:
            cur=self.head
            while cur.next.next!=None:
                cur=cur.next
            cur.next=None
    
    def display(self):
        cur=self.head
        while cur.next!=None:
            print(cur.data)
            cur=cur.next
        print(cur.data)


llist=LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
print('after adding items at end')
llist.display()

print('after deleting first item from end')
llist.delete_at_end()
llist.display()

print('after deleting second item from end')
llist.delete_at_end()
llist.display()

print('after deleting third item from end')
llist.delete_at_end()
llist.display()

print('after deleting fourth item from end')
llist.delete_at_end()
llist.display()




