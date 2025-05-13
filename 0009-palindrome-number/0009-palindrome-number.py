class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_n = list(str(x)) # stores the given interger as a list of str values eg: ['1','2','1]
        for i in range(len(list_n)//2):
            # Iam using 2 pointer approach where which checks if the element in the begining is equal to the element at the end . if any one condition fails return False
            if list_n[i] !=list_n[-i-1]:
                return False
        return True
