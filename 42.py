class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        if n == 0:
            return 0
        left = [ 0 for i in range(n) ]
        right = [ 0 for i in range(n) ]
        mx = 0
        for i in range(n):
            left[i] = mx
            mx = max(mx, A[i])
        mx = 0
        for i in range(n - 1, -1, -1):
            right[i] = mx
            mx = max(mx, A[i])
        res = 0
        for i in range(n):
            if min(left[i], right[i]) < A[i]:
                continue
            res += min(left[i], right[i]) - A[i]
        return res