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


    llist.printList()
