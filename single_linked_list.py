class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

llist1=LinkedList()
llist1.head=Node('Mon')

llist2=Node('Tue')
llist1.head.next=llist2

llist3=Node('Wed')
llist2.next=llist3

llist4=Node('Thu')
llist3.next=llist4

llist5=Node('Fri')
llist4.next=llist5

llist6=Node('Sat')
llist5.next=llist6

llist7=Node('Sun')
llist6.next=llist7

llist6.printlist()
