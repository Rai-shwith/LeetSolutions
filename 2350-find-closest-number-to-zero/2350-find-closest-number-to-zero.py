from functools import reduce
class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest_number = reduce(lambda x, y : x if abs(x)<abs(y) else y ,nums)
        if abs(closest_number) in nums:
            closest_number = abs(closest_number)
        return closest_number