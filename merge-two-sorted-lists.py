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
        count=self.getCount()
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
        return
            
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data, end="->")
            temp=temp.next

def mergelist(head1,head2):
        temp=None

        if(head1 is None):
            return head2
        if(head2 is None):
            return head1

        if(head1.data<=head2.data):
            temp=head1
            temp.next=mergelist(head1.next,head2)

        else:
            temp=head2
            temp.next=mergelist(head1,head2.next)

        return temp

if __name__ =='__main__':
    llist1=LinkedList()
    llist2=LinkedList()
    
    llist1.push(32)
    llist1.push(90)
    llist1.push(33)
    llist1.push(525)
    llist1.push(10)
    llist1.push(277)
    llist1.push(129)
    llist1.sort()

    llist2.push(19)
    llist2.push(101)
    llist2.push(33)
    llist2.push(25)
    llist2.push(0)
    llist2.push(64)
    llist2.push(167)
    llist2.sort()

    llist3=LinkedList()
    llist3.head = mergelist(llist1.head,llist2.head)

    llist3.printlist()
