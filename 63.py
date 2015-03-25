class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
            
        dp = [ [ 0 for j in range(n + 1) ] for i in range(m + 1) ]
        dp[1][1] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i-1][j-1] == 1 or (i == 1 and j == 1):
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]