class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def dfs(self, st, par_sum):
        if par_sum == self.tar:
            self.res.add(tuple(self.ve))
            return
        
        if st >= self.n or par_sum > self.tar or par_sum + self.sum[st] < self.tar:
            return 
        
        for i in range(st, self.n):
            if par_sum + self.a[i] > self.tar:
                continue
            self.ve.append(self.a[i])
            self.dfs(i + 1, par_sum + self.a[i])
            self.ve.pop()
            
    def combinationSum2(self, candidates, target):
        n = len(candidates)
        if n == 0:
            return [ [] ]
            
        candidates.sort()
        self.n = n
        self.a = candidates
        self.tar = target
        self.ve = []
        self.res = set()
        self.sum = [ 0 for i in range(n) ]
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                self.sum[i] = candidates[i]
            else:
                self.sum[i] = candidates[i] + self.sum[i+1]
        
        self.dfs(0, 0)
        
        res = []
        for ret in self.res:
            res.append(list(ret))
        return res