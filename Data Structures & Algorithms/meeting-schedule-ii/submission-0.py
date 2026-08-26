"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end=sorted([i.end for i  in intervals])

        res=count=0
        S=E=0

        while S<len(intervals):
            if start[S]<end[E]:
                S+=1
                count+=1
                # new meeting starts before the meeting ends
            else:
                E+=1
                count-=1
                # meeting ends before the new meeting starts
            res=max(res,count)
        return res

