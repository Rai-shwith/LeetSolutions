class Solution:
  def pivotInteger(self, n: int) -> int:
    result=((n**2+n)/2)**0.5
    print(result)
    if result==int(result):
      return int(result)
    else:
      return -1
