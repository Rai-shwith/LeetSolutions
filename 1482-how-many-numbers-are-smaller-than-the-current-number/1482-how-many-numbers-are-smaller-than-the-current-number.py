class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i,j in enumerate(nums):
            for _,l in enumerate(nums,i):
                if l < j:
                    result[i]+=1
        return result
        