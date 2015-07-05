class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        dp = {0: [], 1: []}
        cur = 0
        for row in triangle:
            n = len(row)
            if n == 1:
                dp[cur].append(row[0])
            else:
                for i in range(n):
                    if i == n - 1:
                        dp[cur].append(dp[cur^1][i-1] + row[i])
                    elif i == 0:
                        dp[cur][i] = dp[cur^1][0] + row[i]
                    else:
                        dp[cur][i] = min(dp[cur^1][i-1], dp[cur^1][i]) + row[i]
            dp[cur^1] = []
            for item in dp[cur]:
                dp[cur^1].append(item)
            cur ^= 1
        n = len(triangle)
        res = 1<<30
        for i in range(n):
            res = min(res, dp[cur^1][i])
        return res
            
        
