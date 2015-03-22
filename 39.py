class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def dfs(self, st, c_sum):
        if c_sum == self.target:
            self.res.add(tuple(self.ve))
            return 
        n = len(self.a)
        if st >= n:
            return
        for i in range(st, n):
            if self.a[i] + c_sum > self.target:
                continue
            self.ve.append(self.a[i])
            self.dfs(i, c_sum + self.a[i])
            self.ve.pop()
            self.ve.append(self.a[i])
            self.dfs(i + 1, c_sum + self.a[i])
            self.ve.pop()
        
    def combinationSum(self, candidates, target):
        a = candidates
        a.sort()
        self.a = a
        self.target = target
        self.ve = []
        self.res = set()
        n = len(a)
        if n == 0:
            return  [ [] ]
                
        self.dfs(0, 0)
        res = []
        for i in self.res:
            res.append(list(i))
        return res