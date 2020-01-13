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

    def insert_at_index(self,index,data):
        if index==1:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            return
        i=1
        cur=self.head
        while i<index-1 and cur.next!=None:
            cur=cur.next
            i+=1
        if cur.next==None:
            print(index,'index out of range')
        else:
            new_node=Node(data)
            new_node.next=cur.next
            cur.next=new_node

llist=LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
llist.insert_at_end(80)
llist.display()
llist.insert_at_index(2,200)
llist.insert_at_index(5,300)
llist.insert_at_index(8,500)
llist.display()
