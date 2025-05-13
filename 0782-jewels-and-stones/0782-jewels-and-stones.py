class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_bag: set[str] = set(jewels)
        count: int = 0
        for i in stones:
            if i in jewels_bag:
                count+=1
        return count