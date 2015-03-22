class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def lower_bound(self, A, target):
        first = 0
        length = len(A)
        
        while length > 0:
            half = length / 2
            middle = first + half
            if A[middle] < target:
                first = middle + 1
                length = length - half - 1
            else:
                length = half
        return first
    
    def upper_bound(self, A, target):
        first = 0
        length = len(A)
        
        while length > 0:
            half = length / 2
            middle = first + half
            if A[middle] > target:
                length = half
            else:
                first = middle + 1
                length = length - half - 1
        return first
        
    def searchRange(self, A, target):
        n = len(A)
        if n == 0:
            return [-1, -1]
        x = self.lower_bound(A, target)
        if x == n or A[x] != target:
            return [-1, -1]
        y = self.upper_bound(A, target)
        return [x, y-1]