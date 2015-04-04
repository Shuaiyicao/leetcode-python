class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n = len(s)
        if n == 0:
            return 0
        dp = [ 0 for i in range(n + 1) ]
        dp[0] = 1
        for i in range(1, n + 1):
            if i == 1:
                dp[i] = 1 if int(s[0]) >= 1 else 0
                continue
            if str(int(s[i-2:i])) == s[i-2:i] and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            if int(s[i-1:i]) >= 1:
                dp[i] += dp[i-1]
        return dp[n]