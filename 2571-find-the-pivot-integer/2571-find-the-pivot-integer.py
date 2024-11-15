class Solution:
  def pivotInteger(self, n: int) -> int:
    if n==1:
      return 1
    for i in range(n):
      if sum(range(1,i+1))==sum(range(i,n+1)):
        return i
    else:    
      return -1