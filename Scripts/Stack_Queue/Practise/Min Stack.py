class MinStack:
    """Creation of the class for getting the minimum element in a stack in an o(1) operation"""
    # Initialization of the variables
    def __init__(self):
        self.items = []
        self.minimum=[float('inf')]

    # Push function for appending element in the Stack
    def push(self, x: int) -> None:
        self.items.append(x)
        # Checking if the element is not there in the list of minimum and also checking that whether the integer X is less than the minimum.
        if x not in self.minimum and x< self.minimum[-1]:
            self.minimum.append(x)

    def pop(self) -> int:
        """Removing the element from the end from the list"""
        if len(self.items) == 0:
            return -1
        x=self.items.pop()
        # If the removed element and the minimum element are same then remove from the minimum also.
        if x==self.minimum[-1]:
            self.minimum.pop()
        return x

    def top(self) -> int:
        """Get the top element from the list"""
        if len(self.items) == 0:
            return -1
        return self.items[-1]

    def is_empty(self) -> bool:
        """Check if the list is empty"""
        return len(self.items) == 0

    def size(self) -> int:
        """Get the size of the list"""
        return len(self.items)

    def get_min(self) -> float:
        """Get the minimum element of the Stack"""
        if len(self.minimum) == 0:
            raise IndexError("The list of minimum element is empty")
        return self.minimum[-1]

stack = MinStack()  # Creation of object from the class

#region Appending_Element
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(1)
stack.push(2)
#endregion

#region Printing_All_Variables
print(f"Stack Content      : {stack.items}")
print(f"Current Minimum    : {stack.get_min()}")

print(f"Popped Element     : {stack.pop()}")

print(f"Stack After Pop    : {stack.items}")
print(f"Current Minimum    : {stack.get_min()}")

stack.push(-1)

print(f"Stack After Push   : {stack.items}")
print(f"Current Minimum    : {stack.get_min()}")
print(f"Popped Element     : {stack.pop()}")
print(f"Current Minimum    : {stack.get_min()}")
print(f"Top Element        : {stack.top()}")
print(f"Stack Size         : {stack.size()}")
print(f"Is Stack Empty?    : {stack.is_empty()}")
#endregion