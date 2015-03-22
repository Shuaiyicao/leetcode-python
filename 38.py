class Solution:
    # @return a string
    def __init__(self):
        self.res = ['', '1', '11', '21', '1211']
        for i in range(5, 20):
            self.res.append(self.int_to_str(self.res[-1]))
            
    def int_to_str(self, s):
        n = len(s)
        res = ''
        i = 0
        while i < n:
            cnt = 1
            if i < n - 1 and s[i] == s[i+1]:
                while i < n - 1 and s[i] == s[i+1]:
                    cnt += 1
                    i += 1
                i += 1
            else:
                i += 1
            res += str(cnt) + s[i-1]
        return res
                
    def countAndSay(self, n):
        if n < len(self.res):
            return self.res[n]
        else:
            m = len(self.res)
            for i in range(m, n + 1):
                self.res.append(self.int_to_str(self.res[-1]))
            return self.res[n]