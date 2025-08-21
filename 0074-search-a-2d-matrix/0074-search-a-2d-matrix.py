class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n-1
        while low <= high:
            mid = (high+low)//2
            i = mid//n
            j = mid%n
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                low = mid+1
            else:
                high = mid-1
        return False
        