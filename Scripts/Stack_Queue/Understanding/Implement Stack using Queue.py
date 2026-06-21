from collections import deque
from typing import List

class StackFromQueue:
    def __init__(self)->None:
        self.items = deque()

    def is_empty(self)->bool:
        return self.items == []

    def push(self, item)->None:
        self.items.appendleft(item)

    def pop(self)->int:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def top(self)->int:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def size(self)->int:
        return len(self.items)

st=StackFromQueue()
st.push(1)
st.push(2)
st.push(3)
st.push(4)

print(f"Top Element : {st.top()}")
print(f"Stack Size  : {st.size()}")
print(f"Popped Item : {st.pop()}")
print(f"Top After Pop : {st.top()}")
print(f"Is Stack Empty? : {st.is_empty()}")
print(f"Current Stack Size : {st.size()}")