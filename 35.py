class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def lower_bound(self, A, n, target):
        first = 0
        last = n
        len = last - first
        while len > 0:
            half = len / 2
            middle = first + half
            if A[middle] < target:
                first = middle + 1
                len = len - half - 1
            else:
                len = half
        return first
        
    def searchInsert(self, A, target):
        return self.lower_bound(A, len(A), target)