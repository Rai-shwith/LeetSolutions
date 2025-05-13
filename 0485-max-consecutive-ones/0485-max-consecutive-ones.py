class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        final = 0 # Counter to store the final answer
        current = 0 # Counter to keep track of current consecutive ones
        for i in nums:
            if i == 1:
                current += 1
                if current > final:
                    final = current
            else:
                current = 0
        return final

        