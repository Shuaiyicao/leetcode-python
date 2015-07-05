class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if T == "":
            return 1
        if S == "":
            return 0
            
        n = len(S)
        m = len(T)
        dp = [[ 0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if S[i-1] == T[j-1] else 0)
        return dp[n][m]
                
