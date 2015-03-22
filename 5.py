class Solution:
    # @return a string
    
    def longestPalindrome(self, s):
        n = len(s)
        if n == 0:
            return ''
        if n == 1:
            return s
            
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
                    
        k = 1
        res = a[1]
        for i in range(1, n):
            if extend[i] > k:
                k = extend[i]
                res = a[i-extend[i]:i+extend[i]+1]
        return ''.join([i for i in res if i != '#'])