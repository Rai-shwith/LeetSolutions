class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for i in sorted(asteroids):
            if mass < i:
                return False
            mass+=i
        else:
            return True