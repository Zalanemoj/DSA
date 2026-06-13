nums=[9,5,7]

result=[]
def power_set(index,subset):
    if index >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[index])
    power_set(index+1,subset)
    subset.pop()
    power_set(index+1,subset)

power_set(0,[])
print(result)

# Time Complexity ----> o(2^n)
# Space Complexity ----> o(n)