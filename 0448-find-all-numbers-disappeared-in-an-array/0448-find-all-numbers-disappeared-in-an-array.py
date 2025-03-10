class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        unique_set = set(nums)
        full_set = set(range(1,length+1))
        return list(full_set - unique_set)