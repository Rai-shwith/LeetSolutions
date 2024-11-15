class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_n = list(str(x))
        for i in range(len(list_n)//2):
            if list_n[i] !=list_n[-i-1]:
                return False
        return True
        