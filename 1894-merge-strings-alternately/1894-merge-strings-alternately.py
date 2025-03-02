class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        long_word = word1 if len(word1) > len(word2) else word2
        short_word = word1 if len(word1) < len(word2) else word2
        altered_word = ""
        i:int = 0
        while i<len(long_word):
            if i == len(short_word):
                altered_word+=long_word[i:]
                break
            altered_word+=word1[i]
            altered_word+=word2[i]
            i+=1
        return altered_word