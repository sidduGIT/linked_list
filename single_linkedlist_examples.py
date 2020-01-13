class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class single_linkedlist:

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

    def insert_at_start(self,data):
        if self.head==None:
            new_node=Node(data)
            self.head=new_node
            return
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

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

llist=single_linkedlist()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.display()
llist.insert_at_start(5)
llist.display()
llist.insert_at_start(3)
llist.display()
llist.insert_at_start(1)
llist.display()
