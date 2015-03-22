class Solution:
    # @return an integer
    def reverse(self, x):
        neg = False
        if x < 0:
            neg = True
            x = -x
        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x /= 10
        if neg:
            res = -res
        return res