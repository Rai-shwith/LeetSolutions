class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       counter_s:int = 0
       counter_t:int = 0
       while counter_s < len(s):
            while True:
               if counter_t >= len(t):
                   return False
               if t[counter_t] == s[counter_s]:
                   t = t[counter_t+1:]
                   counter_t=0
                   break
               counter_t+=1
            counter_s+=1
       return True