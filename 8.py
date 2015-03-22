class Solution:
    # @return an integer
    def atoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s = str
        n = len(str)
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        if i == n or not(s[i].isdigit() or s[i] == '+' or s[i] == '-'):
            return 0
        
        neg = False
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            neg = True
            i += 1
        
        res = 0
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        if neg:
            res = -res
            
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res