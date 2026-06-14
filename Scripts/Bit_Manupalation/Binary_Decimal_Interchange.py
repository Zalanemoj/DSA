class Solution:

    def decimal_to_binary(self, num: int) -> str:
        if num == 0:
            return '0'
        result=""
        while num > 0:
            if num%2==1:
                result+="1"
            else:
                result+='0'
            num=num//2
        result=result[::-1]
        return result

    def binary_to_decimal(self, num: str) -> int:
        if num == 0:
            return 0
        result=0
        for i in range(0,len(num)):
            result+=int(num[i])*(2**i)

        return result

sol=Solution()
print(sol.decimal_to_binary(5))
print(sol.binary_to_decimal("101"))