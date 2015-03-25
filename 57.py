# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def overlap(self, a, b):
        if a.start > b.start:
            a, b = b, a
        if b.start > a.end:
            return False
        return True
        
    def merge(self, a, b):
        if a.start > b.start:
            a, b = b, a
        return Interval(a.start, max(a.end, b.end))
        
    def insert(self, intervals, newInterval):
        res = []
        for item in intervals:
            if self.overlap(item, newInterval):
                newInterval = self.merge(item, newInterval)
            else:
                res.append(item)
        res.append(newInterval)
        return sorted(res, key= lambda i: i.start)