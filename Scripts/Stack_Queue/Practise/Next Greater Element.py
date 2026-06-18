from typing import List
class Solution:

    def __init__(self):
        """Initializing all the variables required for the class"""
        self.nums=[19,4,2,11,6,5,3,10]
        self.ans=[-1]*(len(self.nums))
        self.stack=[]

    def next_greater_element(self)->List:
        """Finding the greatest element next to the current element and returning the list of result"""
        for i in range(len(self.nums)-1,-1,-1):
            while self.stack and self.stack[-1]<=self.nums[i]:
                self.stack.pop()
            if len(self.stack) !=0:
                self.ans[i]=self.stack[-1]
            self.stack.append(self.nums[i])

        return self.ans

sol=Solution()
print(sol.next_greater_element())