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
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def display(self):
        if self.head==None:
            print('linked list has no elements')
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
        print('Nuber of nodes in the linked list',count)

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
            print('element found')
        else:
            print('element not found')

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
first.display()
first.size()
first.search(160)
