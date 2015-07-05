class Solution:
    # @param A, a list of integers
    # @return an integer
    
    def maxProduct(self, A):
        n = len(A)
        self.dp = [ [A[i], A[i]] for i in range(n) ]
        res = max(A)
        for i in range(1, n):
            x = min(self.dp[i-1][0] * A[i], self.dp[i-1][1] * A[i])
            y = max(self.dp[i-1][0] * A[i], self.dp[i-1][1] * A[i])
            self.dp[i][0] = min(self.dp[i][0], x)
            self.dp[i][1] = max(self.dp[i][1], y)
            res = max(res, self.dp[i][1])
        return res