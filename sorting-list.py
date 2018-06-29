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

    def getCount(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return(count)

    def sort(self):
        count=llist.getCount()
        prev=self.head
        for j in range(count-1):
            prev=self.head
            for i in range(count-1-j):
                current=prev.next
                if(current.data<prev.data):
                    temp=prev.data
                    prev.data=current.data
                    current.data=temp
                prev=current
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

    print("The Sorted List is")
    llist.sort()
        
