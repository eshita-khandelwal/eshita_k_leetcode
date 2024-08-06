class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
         
       #the idea is we keep track of the previous end. and compare the start point to see if an overlapping event is there or not. if there then we delete the event which has max end point because it has a high chance of overlapping with other next events.
        intervals = sorted(intervals) 
        prevend = intervals[0][1]
        res = 0
        for start,end in intervals[1:]:
            if start>=prevend:
                prevend = end
            else:
                res+=1
                prevend = min(prevend,end)
        return res
