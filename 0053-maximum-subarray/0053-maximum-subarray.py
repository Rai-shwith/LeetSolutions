class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if (sum>res): 
                res = sum
            if (sum<0): # if the sum is negative discard it
                sum = 0
        return res