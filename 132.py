class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if len(s) < 2:
            return 0
        n = len(s)
        a = '#'
        for i in range(n):
            a += s[i] + '#'
        n = len(a)
        extend = [ 0 for i in range(n) ]
        
        #initialize
        center = 0
        right = 0
        
        for i in range(1, n):
            ii = 2 * center - i
            if i >= right:
                extend[i] = 0
            else:
                extend[i] = min(right - i, extend[ii])
                
            while i - extend[i] - 1 >= 0 and i + extend[i] + 1 < n and a[i-extend[i]-1] == a[i+extend[i]+1]:
                extend[i] += 1
                
            if i + extend[i] > right:
                center = i
                right = i + extend[i]
        dp = [ 1<<30 for i in range(n) ]
        xp = [ [] for i in range(n) ]
        
        for i in range(n):
            if a[i] == '#':
                if extend[i] > 0:
                    j = i - extend[i] + 1
                    k = i + extend[i] - 1
                    while j < k:
                        xp[k/2].append(j/2)
                        j += 1
                        k -= 1
            else:
                if extend[i] == 1:
                    xp[i/2].append(i/2)
                else:
                    j = i - extend[i] + 1
                    k = i + extend[i] - 1
                    xp[k/2].append(j/2)
        dp[0] = 0
        for i in range(1, n/2):
            dp[i] = dp[i-1] + 1
            for p in xp[i]:
                if p == 0:
                    dp[i] = 0
                else:
                    dp[i] = min(dp[i], dp[p-1] + 1)
        
        return dp[n/2-1]
