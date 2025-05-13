class Solution:
    def romanToInt(self, s: str) -> int:
        roman_guid:dict={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        value:int=roman_guid[s[-1]]
        for i in range(len(s)-1):
            if roman_guid[s[i]]<roman_guid[s[i+1]]:
                value-=roman_guid[s[i]]
            else:
                value+=roman_guid[s[i]]
        return value