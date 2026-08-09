class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        prevEnd=intervals[0][1]

        for start , end in intervals[1:]:
            if start >= prevEnd:
                prevEnd=end
            # start<prevEnd: overlapping 
            # remove the interval which ends first to minimize the no. of overlapping intervals
            else:
                count+=1
                prevEnd=min(prevEnd,end)
        
        return count


        