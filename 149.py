# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def gao(self, a, b):
        if a.x == b.x:
            return 1<<30
        return (1.0 * b.y - a.y) / (b.x - a.x)
    def mx(self, lists):
        n = len(lists)
        if n == 0:
            return 0
        lists.sort()
        i = 0
        res = 1
        while i + 1 < n:
            if abs(lists[i] - lists[i+1]) < 1e-4:
                tmp = 1
                while i + 1 < n and abs(lists[i] - lists[i+1]) < 1e-4:
                    i += 1
                    tmp += 1
                i += 1
                res = max(res, tmp)
            else:
                i += 1
                
        return res
            
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        n = len(points)
        res = 2
        for i in xrange(n):
            lists = []
            same = 1
            for j in xrange(i + 1, n):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same += 1
                else:
                    lists.append(self.gao(points[i], points[j]))
            res = max(res, self.mx(lists) + same)
        return res
                
