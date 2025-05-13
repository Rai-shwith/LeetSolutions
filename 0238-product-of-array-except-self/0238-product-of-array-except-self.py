class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n:int=len(nums)
        left_product:list=[1]*n
        right_product:list=[1]*n
        for i in range(1,n):
            left_product[i]=left_product[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right_product[i]=right_product[i+1]*nums[i+1]
        product_list:list[int]=[left_product[i]*right_product[i] for i in range(n)]
        return product_list
    