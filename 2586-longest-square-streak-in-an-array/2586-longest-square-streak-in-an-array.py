from math import sqrt
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums: set = set(nums) # for better searching which takes O(n) for set
        counts = [] 
        for num in nums:
            root : float = sqrt(num)
            count = 1
            while root == int(root) and root in nums : # checks is it complete square and if the root is present in the given nums
                count+=1
                root = sqrt(root)
            counts.append(count)
        streak = max(counts)
        return streak if streak !=1 else -1 # returns -1 if the streak is 1
        