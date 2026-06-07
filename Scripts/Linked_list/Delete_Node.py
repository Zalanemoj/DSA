class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node

    def traversal(self):
        if self.head is None:
            print("Empty List")
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" ")
                current=current.next

    def insert(self, value,position):
        new_node=Node(value)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            previous=None
            count=0
            while current is not None and count < position:
                previous=current
                current=current.next
                count+=1
            previous.next=new_node
            new_node.next=current

    def delete(self,value):
        temp = self.head
        if temp is not None:
            if self.head == value:
                self.head=self.head.next
                temp.next = None
            else:
                found=False
                previous=None
                while temp is not None:
                    if temp.value==value:
                        found=True
                        break
                    previous=temp
                    temp=temp.next
                if found:
                    previous.next=temp.next
                    return
                else:
                    print("Not found")



# ll=LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# ll.append(40)
# ll.insert(75,2)
# ll.delete(20)
# ll.traversal()