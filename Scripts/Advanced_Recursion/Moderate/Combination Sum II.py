nums=[1,1,2,1,2]

target=5

class Solution:

    def solve(self,index:int,total:int,numbers:list,subset:list,result:list)->None:
        if total == target:
            subset.sort()
            if subset in result:
                return
            else:
                result.append(subset.copy())
            return

        if total > target:
            return

        if index >= len(numbers):
            return

        # Pick an index
        subset.append(numbers[index])
        sum=total + numbers[index]
        self.solve(index+1,sum,numbers,subset,result)

        # Not pick a number
        subset.pop()
        sum=total
        self.solve(index+1,sum,numbers,subset,result)


    def combination_sum(self,candidates:list)->list:
        result=[]

        global target
        global nums

        nums=candidates

        self.solve(0,0,nums,[],result)
        return result

sol=Solution()
print(sol.combination_sum(nums))