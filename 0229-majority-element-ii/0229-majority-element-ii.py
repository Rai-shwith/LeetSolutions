class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n:int = len(nums)
        count1:int = 0
        count2:int = 0
        ele1:int|None = None
        ele2:int|None = None
        for num in nums:
            if count1 == 0 and ele2 != num:
                count1 = 1
                ele1 = num
            elif count2 == 0 and ele1 != num :
                count2 = 1
                ele2 = num
            elif ele1 == num:
                count1+=1
            elif ele2 == num:
                count2+=1
            else:
                count1-=1
                count2-=1
            
        count1=0
        count2=0
        for num in nums:
            count1+=1 if num == ele1 else 0
            count2+=1 if num == ele2 else 0
        res = []
        res.append(ele1) if count1 > n//3 else 0
        res.append(ele2) if count2 > n//3 else 0
        return res
