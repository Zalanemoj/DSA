class Solution:

    def solve(self,index,flag,numbers,result):
        if index >= len(numbers):
            result.append("".join(numbers))
            return
        numbers[index]="0"
        self.solve(index+1,True,numbers,result)
        if flag:
            numbers[index]="1"
            self.solve(index+1,False,numbers,result)
            numbers[index]="0"

    def generate_binary_strings(self,n):
        result=[]
        numbers=["0"]*n
        self.solve(0,True,numbers,result)
        return result

sol=Solution()
print(sol.generate_binary_strings(3))