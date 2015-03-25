class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 2:
            return x
        first = 1
        last = x + 1
        len = last - first
        while len > 0:
            half = len / 2
            middle = first + half
            if middle * middle < x:
                first = middle + 1
                len = len - half - 1
            else:
                len = half
        if first * first == x:
            return first
        else:
            return first - 1