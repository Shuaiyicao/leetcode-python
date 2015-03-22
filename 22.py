class Solution:
    # @param an integer
    # @return a list of string
    def dfs(self, left, right):
        if left == self.n and right == self.n:
            self.res.append(str(self.ve))
            return
        if len(self.stack) == 0:
            self.ve += '('
            self.stack.append(0)
            self.dfs(left + 1, right)
            self.ve = self.ve[:-1]
            self.stack.pop()
        else:
            self.stack.pop()
            self.ve += ')'
            self.dfs(left, right + 1)
            self.stack.append(0)
            self.ve = self.ve[:-1]
            
            if left < self.n:
                self.ve += '('
                self.stack.append(0)
                self.dfs(left + 1, right)
                self.ve = self.ve[:-1]
                self.stack.pop()
                
    def generateParenthesis(self, n):
        if n == 0:
            return []
        self.ve = ''
        self.stack = []
        self.res = []
        self.n = n
        self.dfs(0, 0)
        return self.res