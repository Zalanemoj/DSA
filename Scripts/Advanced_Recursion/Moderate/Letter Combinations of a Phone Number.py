class Solution:

    def __init__(self)->None:
        self.digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def solve(self,digit,result:list,index:int,subset:list)->None:
        if index >= len(digit):
            result.append("".join(subset))
            return

        letter=self.digits_to_letters.get(digit[index],"")

        for char in letter:
            subset.append(char)
            self.solve(digit,result,index+1,subset)
            subset.pop()

    def combine_digits(self,digits:str)->list:
        result=[]
        if not digits:
            return []

        self.solve(digits,result,0,[])

        return result

sol=Solution()

print(sol.combine_digits("9999"))
