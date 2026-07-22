class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hashmap = dict()

        for num in prices:
            if num not in hashmap:
                hashmap[num] = prices[num]

        profit = 0

        for num in hashmap:
            profit=max(profit+hashmap[num],profit)

        return profit