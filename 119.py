class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        dp = { 0: [], 1: [ 1 ] }
        cur = 0
        for i in range(rowIndex):
            dp[cur] = []
            for j in range(i + 2):
                if j == 0:
                    dp[cur].append(dp[cur^1][0])
                elif j == i + 1:
                    dp[cur].append(dp[cur^1][i])
                else:
                    dp[cur].append(dp[cur^1][j-1] + dp[cur^1][j])
            dp[cur^1] = []
            for item in dp[cur]:
                dp[cur^1].append(item)
            cur ^= 1
        return dp[cur^1]
                    
