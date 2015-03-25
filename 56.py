# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def overlap(self, a, b):
        if a.start > b.start:
            a, b = b, a
        if b.start > a.end:
            return False
        return True
        
    def Merge(self, a, b):
        if a.start > b.start:
            a, b = b, a
        return Interval(a.start, max(a.end, b.end))
        
    def merge(self, intervals):
        stack = []
        intervals.sort(key=lambda i: i.start)
        for item in intervals:
            if len(stack) == 0 or not self.overlap(stack[-1], item):
                stack.append(item)
                continue
            while len(stack) > 0 and self.overlap(stack[-1], item):
                tmp = stack.pop()
                item = self.Merge(item, tmp)
            stack.append(item)
        return stack