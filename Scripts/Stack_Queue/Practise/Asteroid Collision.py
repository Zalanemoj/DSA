from typing import List

class Solution:

    def __init__(self):
        """Initialization of all the variables required from the problem"""
        self.nums=[4,7,1,1,25,-3,-7,17,15,-16]
        self.stack=[]
        self.ans=self.nums.copy()

    def asteroid_collision(self) -> None:
        """ It will provide values related to asteroid collision"""

        # Iterating through each and every element
        for i in range(0,len(self.nums)-1):
            if self.nums[i] > 0:
                self.stack.append(self.nums[i])
                self.ans.remove(self.nums[i])

            while self.stack and self.stack[-1] <= abs(self.nums[i]):
                self.stack.pop()
                self.ans.remove(self.nums[i])

        while self.stack:
            self.ans.append(self.stack.pop())

    def get_asteroid_collision(self) -> List[int]:
        self.asteroid_collision()
        return self.ans

sol=Solution()
print(sol.get_asteroid_collision())