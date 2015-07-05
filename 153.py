class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        n = len(num)
        if n <= 2:
            return min(num)
        if num[-1] > num[0]:
            return num[0]
            
        l = 0
        r = n - 1
        while r > l + 1:
            mid = (l + r) >> 1
            if num[mid] < num[r]:   # right part
                r = mid
            if num[mid] > num[l]:   # left part
                l = mid
        return num[r]