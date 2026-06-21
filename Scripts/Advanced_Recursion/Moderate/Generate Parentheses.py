from ast import List

number_to_which=int(input("Enter the value upto which you want to find parentheses: "))

class Solution:

    def solve(self,index:int,total:int,brackets,result):
        if index >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        if total > len(brackets)//2:
            return
        elif total < 0:
            return

        brackets[index]="("
        sum=1+total
        self.solve(index+1,sum,brackets,result)
        brackets[index]=")"
        sum=total-1
        self.solve(index+1,sum,brackets,result)

    def generate_parenthesis(self, n: int) -> List[str]:
        result=[]
        brackets=[""]*(n*2)
        self.solve(0,0,brackets,result)
        return result

sol=Solution()
print(sol.generate_parenthesis(number_to_which))
