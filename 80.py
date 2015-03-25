class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        res = 0
        for i in range(n):
            if res > 1 and A[i] == A[res-1] and A[i] == A[res-2]:
                continue
            A[res] = A[i]
            res += 1
        return res