class Solution:
    # @return an integer
    def maxArea(self, height):
        n = len(height)
        if n < 2:
            return 0
        right = []
        left = []
        mx = 0
        for i in range(n - 1, -1, -1):
            if height[i] > mx:
                right.append( (i, height[i]) )
                mx = height[i]
            else:
                continue
        mx = 0
        for i in range(n):
            if height[i] > mx:
                left.append( (i, height[i]) )
                mx = height[i]
            else:
                continue
        res = 0
        for i in range(len(left)):
            for j in range(len(right)):
                if left[i][0] == right[j][0]:
                    continue
                res = max(res, abs(left[i][0] - right[j][0]) * min(left[i][1], right[j][1]))
        return res