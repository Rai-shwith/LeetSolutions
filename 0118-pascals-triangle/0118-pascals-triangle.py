class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        soln = []
        for i in range(numRows):
            arr = [1]*(i+1)
            if i >1:
                for j in range(1,i):
                    arr[j]=soln[-1][j-1]+soln[-1][j]
            soln.append(arr)
        return soln
        