class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        low = intervals[0][0]
        high = intervals[0][1]
        res=[]
        for i in range(len(intervals)-1):
            if high>=intervals[i+1][0]:
                high=max(intervals[i+1][1],high)
            else:
                res.append([low,high])
                low = intervals[i+1][0]
                high = intervals[i+1][1]
        res.append([low,high])
        return res