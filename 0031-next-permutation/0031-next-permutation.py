class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rec = []
        l = len(nums)
        for i in range(l-1,-1,-1):# iteration from backwards
            gtn = {j for j in rec if j > nums[i] } # get the numbers greater than the current index number
            rec.append(nums[i])
            if gtn:
                min_value = min(gtn)
                nums[i] = min_value
                i+=1
                rec.remove(min_value)
                # nums[i:]= sorted(rec)
                while (i < l):
                    nums[i] = min(rec)
                    rec.remove(nums[i])
                    i+=1
                return
        nums[:] = sorted(nums)