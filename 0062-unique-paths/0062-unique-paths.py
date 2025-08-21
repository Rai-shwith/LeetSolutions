class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_store=[[-1]*n for i in range(m)]
        def find_path(i,j):
            """Dynamic Programming Approch"""
            if (i>=m or j>=n):
                return 0
            if dp_store[i][j] != -1:
                return dp_store[i][j]
            if (i==m-1 and j==n-1):
                return 1
            path_cost = find_path(i,j+1) + find_path(i+1,j)
            dp_store[i][j]=path_cost
            return path_cost
        return find_path(0,0)

        