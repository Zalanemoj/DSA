class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        x=self.items.pop(0)
        return x

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(f"Dequeued Element: {queue.dequeue()}")
print(f"Front Element: {queue.front()}")
print(f"Queue Size: {queue.size()}")
print(f"Rear Element: {queue.rear()}")
print(f"Is Queue Empty?: {queue.is_empty()}")