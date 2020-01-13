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

    def count_nodes(self):
        count=0
        cur=self.head
        while cur.next!=None:
            count+=1
            cur=cur.next
        print('number of nodes',count)

    def insert_after(self,data,after):
        new_node=Node(data)
        cur=self.head
        while cur.next!=None:
            save=cur.next
            if cur.data==after:
                cur.next=new_node
                new_node=save
        else:
            print(after,'node not found in a list')

    def display(self):
        cur=self.head
        while cur.next!=None:
            print(cur.data)
            cur=cur.next
        print(cur.data)

llist=LinkedList()
print('initial linked list')
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.display()
print('linked list after adding item')
llist.insert_after(500,30)
llist.display()
