class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        res=[intervals[0]]

        for interval in intervals[1:]:

            #overlap-> curent interval's start before the previous interval ends

            if interval[0]<=res[-1][1]:
                res[-1][1]=max(res[-1][1],interval[1])
            
            # no overlap

            else:
                res.append(interval)
        
        return res