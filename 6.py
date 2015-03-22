class Solution:
    # @return a string
    def dfs(self, s, row, pos, nRows, d):   # d = 0 means down, 1 means up
        if pos == len(s):
            return
        self.res[row].append(s[pos])
        if d == 0:
            d = 1 if row + 1 == nRows - 1 else 0
            self.dfs(s, row + 1, pos + 1, nRows, d)
        else:
            d = 0 if row - 1 == 0 else 1
            self.dfs(s, row - 1, pos + 1, nRows, d)
            
    def convert(self, s, nRows):
        self.res = []
        for i in range(nRows):
            self.res.append([])
        if nRows == 1:
            return s
        self.dfs(s, 0, 0, nRows, 0)
        s = ''
        for item in self.res:
            s += ''.join(item)
        return s