class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        while len(s) > 0:
            if s[0] == ' ':
                s = s[1:]
            else:
                break
        while len(s) > 0:
            if s[-1] == ' ':
                s = s[:-1]
            else:
                break
        for item in s:
            if item == ' ':
                return False
        
        ns = ''
        for c in s:
            if c != ' ':
                ns += c
        try:
            t_int = int(ns)
            return True
        except:
            try:
                t_float = float(ns)
                return True
            except:
                return False