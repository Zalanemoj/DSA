from typing import List
from collections import deque

lst=deque()

lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.appendleft(5)


print(lst)
print(lst.pop())
print(lst)