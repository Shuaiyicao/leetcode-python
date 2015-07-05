class Solution:
    # @return a list of lists of integers
    def get_next(self, last):
        n = len(last)
        res = []
        for i in range(n + 1):
            if i == 0:
                res.append(last[0])
            elif i == n:
                res.append(last[i-1])
            else:
                res.append(last[i-1] + last[i])
        return res
                
    def generate(self, numRows):
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(numRows - 1):
            res.append(self.get_next(res[-1]))
        return res
            
