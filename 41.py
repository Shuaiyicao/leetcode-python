class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A.append(-1)
        n = len(A)
        for i in range(n):
            t = A[i]
            if t <= 0 or t >= n or A[t] == t:
                continue
            while t > 0 and t < n and A[t] != t:
                tmp = A[t]
                A[t] = t
                t = tmp
        for i in range(1, n):
            if A[i] != i:
                return i
        return n