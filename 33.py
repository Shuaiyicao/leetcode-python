class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def lower_bound(self, A, target):
        length = len(A)
        first = 0
        while length > 0:
            half = length / 2
            middle = first + half
            if target > A[middle]:
                first = middle + 1
                length = length - half - 1
            else :
                length = half
        return first
    
    def b_search(self, A, target):
        length = len(A)
        first = -1
        last = length - 1
        while first + 1 < last:
            middle = (first + last) / 2
            if A[middle] > target:
                first = middle
            else:
                last = middle
        return last
        
    def search(self, A, target):
        n = len(A)
        if n == 1 or A[-1] > A[0]:
            x = self.lower_bound(A, target)
            if x == n or A[x] != target:
                return -1
            return x
        x = self.b_search(A[1:], A[0])
        x += 1
        y = self.lower_bound(A[:x], target)
        if y == x or A[y] != target:
            z = self.lower_bound(A[x:], target)
            if z == len(A[x:]) or A[z+x] != target:
                return -1
            return z+x
        else:
            return y