class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        cur=self.head
        while(cur.next!=None):
            cur=cur.next
        cur.next=new_node
    
    def display(self):
        cur=self.head
        while(cur.next!=None):
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
        print('size of linked list is',count)

first=LinkedList()
first.head=Node(10)
first.insert(20)
first.insert(30)
first.insert(40)
first.insert(50)
first.insert(60)
first.insert(70)
first.insert(80)
first.insert(90)
first.insert(100)
first.insert(110)
first.insert(120)
first.display()
first.size()
