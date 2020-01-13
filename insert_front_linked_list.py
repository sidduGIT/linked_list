class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def insert_at_front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def display(self):
        if self.head is None:
            print('list is empty')
        else:
            cur=self.head
            while cur is not None:
                print(cur.data)
                cur=cur.next
            #print(cur.data)

llist=LinkedList()
llist.head=Node(10)
llist.insert_at_front(20)
llist.insert_at_front(40)
llist.insert_at_front(60)
llist.insert_at_front(80)
llist.insert_at_front(120)
#llist.display()

llist.insert_at_end(30)
llist.insert_at_end(50)
llist.insert_at_end(70)
llist.insert_at_end(90)
llist.insert_at_end(130)
llist.display()
