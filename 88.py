class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        for i in range(n):
            A.append(0)
        for i in range(m - 1, -1, -1):
            A[i+n] = A[i]
        i = n
        j = 0
        tot = 0
        while i < m + n and j < n:
            if A[i] < B[j]:
                A[tot] = A[i]
                i += 1
            else:
                A[tot] = B[j]
                j += 1
            tot += 1
        while i < m + n:
            A[tot] = A[i]
            tot += 1
            i += 1
        while j < n:
            A[tot] = B[j]
            tot += 1
            j += 1