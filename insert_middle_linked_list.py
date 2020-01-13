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
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=new_node

    def display(self):
        if self.head==None:
            print('list is empty')
        else:
            cur=self.head
            while cur.next!=None:
                print(cur.data)
                cur=cur.next
            print(cur.data)
    
    def size(self):
        count=0
        cur=self.head
        while cur.next!=None:
            count+=1
            cur=cur.next
        count+=1
        print('number of nodes',count)
    
    def search(self,element):
        found=False
        cur=self.head
        while cur.next!=None:
            if cur.data==element:
                found=True
                break
            else:
                found=False
            cur=cur.next
        if found:
            print('element',element,'found')
        else:
            print('element',element,'not found')
    
    def insert_after(self,after,element):
        cur=self.head
        while cur.next!=None:
            if cur.data==after:
                break
            cur=cur.next
        if cur.next==None:
            print(after,'item not in the list')
        else:
            new_node=Node(element)
            new_node.next=cur.next
            cur.next=new_node

llist=LinkedList()
#llist.head=Node(10)
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
llist.insert_at_end(80)
llist.display()
llist.size()
llist.search(50)
llist.insert_after(60,100)
llist.display()
    

