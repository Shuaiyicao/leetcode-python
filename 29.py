class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        x = 0
        y = 0
        if dividend < 0:
            x = 1
            dividend = -dividend
        if divisor < 0:
            y = 1
            divisor = -divisor
        
        a = [ divisor ]
        for i in range(1, 32):
            a.append(a[-1]<<1)
        
        res = 0
        for i in range(31, -1, -1):
            if a[i] <= dividend:
                res += 1<<i
                dividend -= a[i]
        if x^y:
            return -res
        return res
