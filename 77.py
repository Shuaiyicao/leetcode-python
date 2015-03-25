class Solution:
    # @return a list of lists of integers
    def __init__(self):
        self.ve = []
        self.res = []
    def dfs(self, n, k, st, cnt):
        if cnt == k:
            self.res.append(list(self.ve))
            return
        for i in range(st, n + 1):
            self.ve.append(i)
            self.dfs(n, k, i + 1, cnt + 1)
            self.ve.pop()
            
    def combine(self, n, k):
        self.dfs(n, k, 1, 0)
        return self.res