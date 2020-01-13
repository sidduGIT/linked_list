class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:

    def display(self,head):
        cur=head
        while(cur.next!=None):
            print(cur.data)
            cur=cur.next
        print(cur.data)

    def insert(self,head,data):
        new_node=Node(data)
        if head==None:
            return new_node
        else:
            cur=head
        while(cur.next!=None):
            cur=cur.next
        cur.next=new_node
        return head

mylist=Solution()
head=None
for _ in range(int(input())):
    data=input()
    if data==int:
        data=int(input())
    elif data==float:
        data=float(input())
    head=mylist.insert(head,data)
mylist.display(head)
