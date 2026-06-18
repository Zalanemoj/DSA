from typing import List


class Solution:

    def __init__(self):
        self.nums=[2,10,12,1,11]
        self.ans=[-1]*(len(self.nums))
        self.stack=[]
        self.length=len(self.nums)

    def next_greater_element(self) -> None:
        for i in range(2*self.length-1,-1,-1):
            while self.stack and self.stack[-1]<=self.nums[i%self.length]:
                self.stack.pop()

            if i<self.length:
                if len(self.stack):
                    self.ans[i]=self.stack[-1]

            self.stack.append(self.nums[i%self.length])

    def get_next_greater_element(self) -> List:
        self.next_greater_element()
        return self.ans

sol=Solution()
print(sol.get_next_greater_element())