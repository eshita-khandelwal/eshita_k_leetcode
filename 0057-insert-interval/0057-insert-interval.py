class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #consider the edge cases first. 1st edge case is if the interval is smaller than any interval in intervals then we add it to the result and return the remaining intervals by attaching it to the end. 2nd edge case is if the interval is bigger than the current one then just add the current interval to the result. after that we consider that an interval can be overlapping. so for overlapping interval we take min(new[0],interval[i][0]) -> this is the lowest boundary and similarly max(new[1],interval[i][1]). 

        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
        
        res.append(newInterval)
        return res