class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
            
    def reverse(self):
        current=self.head
        prev=None

        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next

        self.head=prev
        llist.printlist()
            

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__ =='__main__':
    llist=LinkedList()

    llist.push(32)
    llist.push(90)
    llist.push(33)
    llist.push(525)
    llist.push(0)
    llist.push(277)
    llist.push(129)

    llist.printlist()

    print("The Reversed List is")
    llist.reverse()
