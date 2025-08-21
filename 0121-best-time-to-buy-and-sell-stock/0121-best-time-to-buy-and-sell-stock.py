class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        buy = float("inf")
        for i in prices:
            if i < buy:
                buy = i
            elif i - buy > maxi:
                maxi = i-buy
        return maxi