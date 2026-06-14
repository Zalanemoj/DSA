nums=[9,5,4,7,2]
result=[]
target=9

def solve(index:int,total:int,subset:list):
    if total == target:
        result.append(subset.copy())
        return True
    elif total > target:
        return False
    if index >= len(nums):
        return False
    subset.append(nums[index])
    sum=total + nums[index]
    pick=solve(index+1,sum,subset)
    if pick:
        return True
    remove_val=subset.pop()
    sum-=remove_val
    not_pick=solve(index+1,sum,subset)
    return not_pick

print(solve(0,0,[]))
