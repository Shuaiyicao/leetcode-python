class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        n = len(s)
        if n == 0:
            return []
            
        dp = [ [ 0 for i in range(n) ] for j in range(n) ]
        for i in range(n):
            for j in range(n):
                if i >= j:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        for i in range(2, n + 1):
            for j in range(n):
                if i + j - 1 >= n:
                    break
                dp[j][i+j-1] = (s[j] == s[j+i-1] and dp[j+1][j+i-2])
        res = []
        for i in range(n):
            if i == 0:
                res.append([ [s[i]] ])
                continue
            tmp = []
            for j in range(i, -1, -1):
                if dp[j][i]:
                    if j - 1 < 0:
                        tmp.append([s[:i+1]])
                        continue
                    for item in res[j-1]:   # all partitions ended at j-1
                        t = list(item)
                        t.append(s[j:i+1])
                        tmp.append(t)
            res.append(tmp)
        return res[n-1]
                    
