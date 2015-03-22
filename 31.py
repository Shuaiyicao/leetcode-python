class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n = len(num)
        if n < 2:
            return num
            
        i = n - 1
        while i > 0 and num[i] <= num[i-1]:
            i -= 1
        l = n - i
        if l == n:
            return sorted(num)
        mi = num[i]
        k = i
        for j in range(i, n):
            if num[j] > num[i-1] and num[j] < mi:
                mi = num[j]
                k = j
        num[i-1], num[k] = num[k], num[i-1]
        return num[:i] + sorted(num[i:])