class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        n = len(A)
        if n == 0:
            return 0
        dp = [ -1<<30 for i in range(n) ]
        dp[0] = A[0]
        res = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], 0) + A[i]
            res = max(res, dp[i])
            
        return res