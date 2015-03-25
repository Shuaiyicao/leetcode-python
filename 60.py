class Solution:
    # @return a string
    def __init__(self):
        self.res = []
        self.perm = [ 1 ]
        for i in range(1, 10):
            t = self.perm[-1] * i
            self.perm.append(t)
            
    def dfs(self, now, n, k):
        m = len(now)
        if m == 1:
            self.res.append(now[0])
            return 
        base = self.perm[m-1]
        t = k / base
        if k % base == 0:
            self.res.append(now[t-1])
            now.remove(now[t-1])
            self.dfs(now, n - 1, base)
        else:
            self.res.append(now[t])
            now.remove(now[t])
            self.dfs(now, n - 1, k % base)
            
    def getPermutation(self, n, k):
        if k > self.perm[n]:
            return ''
        
        ori = [i for i in range(1, n + 1) ]
        self.dfs(ori, n, k)
        return ''.join(str(i) for i in self.res)