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
    

first=LinkedList()
first.head=Node(10)
print('after iniliazing first node')
first.printlist()

print('after adding second node')
second=Node(20)
first.head.next=second
first.printlist()

print('after adding third node')
third=Node(30)
second.next=third
first.printlist()

print('after adding third node')
fourth=Node(40)
third.next=fourth
first.printlist()

print('after adding fifth node')
fifth=Node(50)
fourth.next=fifth
first.printlist()


