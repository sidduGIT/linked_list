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

    def insert_before(self,before,data):
        if self.head==None:
            print(before,'item not found')
            return
        if before==self.head.data: #if we are adding at first item only
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            return
        cur=self.head
        while cur.next!=None:
            if cur.data==before:
                break
            cur=cur.next
        if cur.next==None:
            print(before,'item not found in list')
        else:
            new_node=Node(data)
            new_node.next=cur.next
            cur.next=new_node


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
llist.insert_at_end(80)
llist.insert_at_end(90)
llist.display()
llist.insert_before(20,100)
llist.insert_before(30,200)
llist.insert_before(40,300)
llist.insert_before(50,400)
llist.insert_before(60,500)
llist.insert_before(70,600)
llist.display()

