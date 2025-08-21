class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        za=set()
        for i in range(m):
            zf=False
            for j in range(n):
                if not matrix[i][j]:
                    zf=True
                    za.add(j)
            if zf:
                matrix[i]=[0]*n
        for i in range(m):
            for j in za:
                matrix[i][j]=0
                
                    