from functools import reduce
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = reduce(lambda x,y:x if len(x) < len(y) else y,strs)
        for word in strs:
            while not prefix == word[:len(prefix)]:
                prefix=prefix[:-1]
        if prefix == "":
            return prefix
        return prefix