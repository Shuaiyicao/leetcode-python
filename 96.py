class Solution:
    # @return an integer
    def __init__(self):
        self.dp = { 0 : 1, 1 : 1 }
    def numTrees(self, n):
        if n in self.dp:
            return self.dp[n]
        res = 0
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n - i - 1)
        self.dp[n] = res
        return res