class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if n < 2:
            return 0
        dp = [ 1<<31 for i in range(n) ]
        dp[0] = 0
        reach = 0
        for i in range(n):
            if dp[i] == 1<<31:
                return -1
            if i + A[i] >= n - 1:
                return dp[i] + 1
            for j in range(reach + 1, i + A[i] + 1):
                dp[j] = min(dp[j], dp[i] + 1)
            reach = i + A[i]
        return -1