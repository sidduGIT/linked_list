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

first=LinkedList()
first.head=Node('Mon')
first.insert('Tue')
first.insert('Wed')
first.insert('Thu')
first.insert('Fri')
first.insert('Sat')
first.insert('Sun')
first.display()

family=LinkedList()
family.head=Node('Shivu')
family.insert('Shaila')
family.insert('Jagu')
family.insert('Siddu')
family.insert('Santu')
family.display()

