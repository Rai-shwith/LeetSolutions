class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        current_sum = 0
        max_sum = 0

        for j in range(len(nums)):
            while nums[j] in seen:
                seen.remove(nums[i])
                current_sum -= nums[i]
                i += 1

            seen.add(nums[j])
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

        return max_sum
