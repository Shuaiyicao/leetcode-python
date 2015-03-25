class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def lower_bound(self, line, first, last, value):
        len = last - first
        while len > 0:
            half = len / 2
            middle = first + half
            if line[middle] < value:
                first = middle + 1
                len = len - half - 1
            else:
                len = half
        return first
    
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
            
        n = len(matrix[0])
        if n == 0:
            return False
            
        line = []
        for i in range(m):
            line.append(matrix[i][0])
        k = self.lower_bound(line, 0, m, target)
        
        if k < m and matrix[k][0] == target:
            return True
        if k == 0:
            return False
        
        p = self.lower_bound(matrix[k-1], 0, n, target)
        return p < n and matrix[k-1][p] == target