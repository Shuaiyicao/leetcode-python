class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def Pow(self, x, n):
        if n == 0:
            return 1
        half = self.Pow(x, n / 2)
        half *= half
        if n % 2 == 1:
            half *= x
        return half
        
    def pow(self, x, n):
        mark = n < 0
        n = abs(n)
        return 1.0 / self.Pow(x, n) if mark else self.Pow(x, n)