class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution:
    # @param A, a list of integers
    # @return a boolean
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
    
        
        
    def canJump(self, A):
        if len(A) == 0:
            return True
        n = len(A)
        intervals = []
        for i in range(n):
            intervals.append(Interval(i, i + A[i]))
        stack = []
        intervals.sort(key=lambda i: i.start)
        for item in intervals:
            if len(stack) == 0 or not self.overlap(stack[-1], item):
                stack.append(item)
                continue
            while len(stack) > 0 and self.overlap(stack[-1], item):
                tmp = stack.pop()
                item = self.merge(item, tmp)
            stack.append(item)
        return stack[0].end >= n - 1