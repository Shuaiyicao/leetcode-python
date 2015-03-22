class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n == 0:
            return 0
        i = 0
        tot = 0
        while i < n:
            if i < n - 1 and A[i] == A[i+1]:
                while i < n - 1 and A[i] == A[i+1]:
                    i += 1
                A[tot] = A[i]
                i += 1
                tot += 1
            else:
                A[tot] = A[i]
                tot += 1
                i += 1
        return tot