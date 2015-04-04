class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if len(height) == 0:
            return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            if len(stack) == 0 or height[i] > stack[-1][0]:
                stack.append((height[i], i))
                continue
            while len(stack) > 0 and height[i] <= stack[-1][0]:
                h, idx = stack.pop()
                res = max(res, h * (i - idx))
            stack.append((height[i], idx))
        while len(stack) > 0:
            height, idx = stack.pop()
            res = max(res, height * (n - idx))
        return res