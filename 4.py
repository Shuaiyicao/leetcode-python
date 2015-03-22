class Solution:
    # @return a float
    def Kth(self, A, m, B, n, k):
        if m > n:
            return self.Kth(B, n, A, m, k)
        if m == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
        p = min(m, k / 2)
        q = k - p
        if A[p-1] > B[q-1]:
            return self.Kth(A, m, B[q:], n - q, k - q)
        elif A[p-1] < B[q-1]:
            return self.Kth(A[p:], m - p, B, n, k - p)
        return A[p-1]
        
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if (m + n) % 2 == 1:
            return self.Kth(A, m, B, n, (m + n + 1) / 2)
        return (self.Kth(A, m, B, n, (m + n) / 2) + self.Kth(A, m, B, n, (m + n) / 2 + 1)) / 2.0
