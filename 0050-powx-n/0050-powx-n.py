class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n%2:
                return x*pow(x,n-1)
            return pow(x*x,n//2)
        if n<0:
            x=1/x
        return pow(x,abs(n))
        