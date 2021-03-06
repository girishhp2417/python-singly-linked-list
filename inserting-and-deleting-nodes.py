class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node=Node(new_data)

        new_node.next=self.head
        self.head=new_node

    def addafter(self,prev_node,new_data):
        new_node=Node(new_data)

        new_node.next=prev_node.next
        prev_node.next=new_node

    def append(self,new_data):
        new_node=Node(new_data)

        last=self.head
        while(last.next):
            last=last.next

        new_node.next=None
        last.next=new_node

    def deletepos(self,position):
        temp=self.head
        if(position==0):
            self.head=temp.next
            temp=None
            return

        for i in range(position-1):
            temp=temp.next
            if(temp is None):
                break
        if(temp is None):
            return
        if(temp.next is None):
            return

        next=temp.next.next
        temp.next=None
        temp.next=next

    def deletekey(self,key):
        temp=self.head

        if(temp.data==key):
            self.head=temp.next
            temp=None
            return
        
        while temp is not none:
            if(temp.data==key):
                break
            prev=temp
            temp=temp.next

        prev.next=temp.next
        temp=None
 

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data,)
            temp = temp.next
 
if __name__=='__main__':
    llist=LinkedList()

    llist.push(23)
    llist.push(34)
    llist.push(43)
    llist.append(99)
    llist.append(109)
    llist.addafter(llist.head.next,234)
    llist.addafter(llist.head.next.next,453)
    llist.deletepos(2)


    llist.printList()
