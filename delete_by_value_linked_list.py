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
        cur=self.head
        while cur.next!=None:
            print(cur.data)
            cur=cur.next
        print(cur.data)

    def delete_by_value(self,value):
        if self.head==None:
            print('list is empty')
        if self.head.data==value: #deleting first value
            self.head=self.head.next
            return
        cur=self.head
        while cur.next!=None:
            if cur.next.data==value:
                break
            cur=cur.next
        if cur.next==None:
            print(value,'value not found in list')
        else:
            cur.next=cur.next.next

llist=LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
llist.insert_at_end(50)
llist.insert_at_end(60)
print('after adding items at the end')
llist.display()

print('after deleting by value')
llist.delete_by_value(20)
llist.display()

print('after deleting by value')
llist.delete_by_value(40)
llist.display()


