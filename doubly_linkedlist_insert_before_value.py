class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Doubly_linkedlist:

    def __init__(self):
        self.head=None

    def insert_before_value(self,before,data):
        if self.head==None:
            print('list is empty')
            return
        else:
            cur=self.head
            while (cur.next!=None):
                if cur.data==before:
                    break
                cur=cur.next
            if cur.next==None:
                print(before,'item not found in the list')
            else:
                new_node=Node(data)
                new_node.next=cur
                new_node.prev=cur.prev
                if cur.prev!=None:
                    cur.prev.next=new_node
                cur.prev=new_node
    
    def insert_at_end(self,data):
        if self.head==None:
            new_node=Node(data)
            self.head=new_node
            return
        cur=self.head
        new_node=Node(data)
        while (cur.next!=None):
            cur=cur.next
        cur.next=new_node
        new_node.prev=cur

    
    def display(self):
        cur=self.head
        while(cur.next!=None):
            print(cur.data)
            cur=cur.next
        print(cur.data)

llist=Doubly_linkedlist()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
llist.insert_at_end(70)
llist.insert_at_end(80)
print('linked list after adding elements at the end')
llist.display()
llist.insert_before_value(30,300)
print('after inserting element before 30')
llist.display()
llist.insert_before_value(50,500)
print('after inserting element before 50')
llist.display()
llist.insert_before_value(70,700)
print('after inserting element before 70')
llist.display()
