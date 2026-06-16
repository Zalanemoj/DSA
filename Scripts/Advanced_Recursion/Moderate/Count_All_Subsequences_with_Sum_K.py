nums=[9,5,4,7,2]
result=[]
target=9
count_val=0
def solve(index:int,total:int,subset:list)->None:
    global count_val
    if total == target:
        result.append(subset.copy())
        count_val+=1
        return
    elif total > target:
        return
    if index >= len(nums):
        return
    subset.append(nums[index])
    sum=total + nums[index]
    solve(index+1,sum,subset)
    remove_val=subset.pop()
    sum-=remove_val
    solve(index+1,sum,subset)

solve(0,0,[])
print(count_val)