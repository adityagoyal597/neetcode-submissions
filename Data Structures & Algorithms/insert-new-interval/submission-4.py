class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res=[]
        for i in range(len(intervals)):

            # new interval comes before current interval

            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]

            # new interval comes after the current interval

            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            
            # new interval overlaps with current interval 

            else:
                newInterval=[
                    min(intervals[i][0],newInterval[0]),
                    max(intervals[i][1],newInterval[1])
                ]
        
        res.append(newInterval)
    
        return res