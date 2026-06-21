class StackQueue:

    def __init__(self):
        self.st1=[]
        self.st2=[]

    def is_empty(self) -> bool:
        return self.st1==[] and self.st2==[]

    def push(self, x: int) -> None:
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.st1.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.st1[-1]

queue = StackQueue()
queue.push(1)
queue.push(2)
queue.push(3)

print(f"Current Stack Content : {queue.st1}")
print(f"Top Element           : {queue.peek()}")
print(f"Popped Element        : {queue.pop()}")
print(f"Stack After Pop       : {queue.st1}")
print(f"Top After Pop         : {queue.peek()}")
print(f"Is Stack Empty?       : {queue.is_empty()}")
print(f"Current Stack Size    : {len(queue.st1)}")