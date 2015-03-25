class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if len(matrix) == 0:
            return
        if len(matrix[0]) == 0:
            return
        n = len(matrix); m = len(matrix[0])
        
        first_row = ( 0 in matrix[0] )
        first_col = ( 0 in [ matrix[i][0] for i in range(n) ] )
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row:
            for i in range(m):
                matrix[0][i] = 0 
        
        if first_col:
            for i in range(n):
                matrix[i][0] = 0