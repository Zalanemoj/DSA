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

ll=LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.traversal()