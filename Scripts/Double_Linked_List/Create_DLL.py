class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

n1 = Node(10)
n2 = Node(20)
n1.next = n2
n2.prev = n1

print(n1.value)
print(n2.value)
print(n1.next.value)
print(n2.prev.value)