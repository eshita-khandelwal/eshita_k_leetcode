class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda index:index[0])
        res = []
        newInt = []
        res.append(intervals[0])

        for i in range(1,len(intervals)):
            if intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            else:
                newInt = [min(intervals[i][0],res[-1][0]),max(intervals[i][1],res[-1][1])]
                res.pop(-1)
                res.append(newInt)
        return res