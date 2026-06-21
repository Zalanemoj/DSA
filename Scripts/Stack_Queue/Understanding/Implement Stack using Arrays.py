class Stack:
    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        if len(self.items) == 0:
            return -1
        x=self.items.pop()
        return x

    def top(self) -> int:
        if len(self.items) == 0:
            return -1
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

st=Stack()
st.push(1)
st.push(2)
st.push(50)
print(f" Stack Content = {st}")
print(f"Popped item = {st.pop()}")
print(f" Stack Content = {st}")
print(f"Top item = {st.top()}")
print(f" Stack Content = {st}")
print(f"Is Stack empty ? {st.is_empty()}")
print(f" Stack size = {st.size()}")