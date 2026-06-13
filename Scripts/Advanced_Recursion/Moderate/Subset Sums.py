nums=[5,9,3]

target=5

class Solution:

    def solve(self,index:int,total:int,numbers:list,subset:list,result:list,k)->None:
        if index >= len(numbers):
            sum_list=sum(subset)
            result.append(sum_list)
            return

        # Pick an index
        subset.append(numbers[index])
        self.solve(index+1,total + numbers[index],numbers,subset,result)

        # Not pick a number
        subset.pop()
        self.solve(index+1,total,numbers,subset,result)


    def combination_sum(self,candidates:list)->list:
        result=[]

        global target
        global nums
        k=3
        nums=candidates

        self.solve(0,0,nums,[],result,k)
        result.sort()
        return result

sol=Solution()
print(sol.combination_sum(nums))