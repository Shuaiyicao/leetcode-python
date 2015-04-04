class Solution:
    # @return a list of integers
    def __init__(self):
        self.res = []
        self.vis = set()
        
    def isPower(self, n):
        for i in range(32):
            if 1<<i == n:
                return True
        return False
        
    def dfs(self, num, n):
        self.vis.add(num)
        self.res.append(num)
        for i in range(n):
            if num & (1<<i):
                k = num - (1<<i)
            else:
                k = num + (1<<i)
            if k in self.vis:
                continue
            self.dfs(k, n)
            break
    def grayCode(self, n):
        self.dfs(0, n)
        return self.res