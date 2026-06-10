class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at(self,value,position):
        new_node = Node(value)
        if position == 0:
            self.insert_at_head(new_node)

        current = self.head
        count = 0
        while current is not None and count < position-1:
            current = current.next
            count += 1

        if current is None:
            IndexError('The position is out of bound ')
            return

        new_node.prev = current
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def traverse(self):
        current = self.head
        if self.head is None:
            print('No elements are there in the list')
            return
        while current is not None:
            print(current.value)
            current = current.next

    def delete_head(self):
        current = self.head
        if self.head is None:
            print('No elements are there in the list')
            return
        self.head=current.next
        current.next = None
        self.head.prev = None

    def delete_last(self):
        current = self.head
        previous = None
        if self.head is None:
            print('No elements are there in the list')
            return
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None
        current.prev = None

    def delete_at_position(self,position):
        if position == 0:
            self.delete_head()
            return
        current = self.head
        count = 0
        while current is not None and count < position-1:
            current = current.next
            count += 1
        if current.next is None:
            self.delete_last()
            return

        current.next = current.next.next
        current.next.next.prev = current


dll = DoubleLinkedList()
dll.insert_at_head(5)
dll.append('A')
dll.append('B')
dll.append('C')
dll.delete_at_position(1)
dll.traverse()
