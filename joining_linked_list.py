class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def display(self):
        if self.next==None:
            print(self.data)
            return
        cur=self.next
        while cur.next!=None:
            print(cur.data)
            cur=cur.next
        print(cur.data)

print('displaying single nodes')
node1=Node(10)
node1.display()
node2=Node(20)
node2.display()
node3=Node(30)
node3.display()
node4=Node(40)
node4.display()
node5=Node(50)
node5.display()

print('now joining individual nodes')
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node1.display()

