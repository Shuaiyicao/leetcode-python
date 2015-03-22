class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        if n == 0:
            return [ [] ]
        for i in range((n + 1) / 2):
            # i, n - i - 1
            tmp = matrix[i][i:n-i]
            
            p = q = i
            x = i; y = n - i - 1
            for j in range(i, n - i):
                matrix[x][y] = matrix[p][q]
                p += 1; y -= 1;
            
            p = n - i - 1; q = i;
            x = y = i;
            for j in range(i, n - i):
                matrix[x][y] = matrix[p][q]
                q += 1; x += 1;
                
            p = q = n - i - 1
            x = n - i - 1; y = i
            for j in range(i, n - i):
                matrix[x][y] = matrix[p][q]
                p -= 1; y += 1
                
            x = i; y = n - i - 1;
            p = 0
            for j in range(i, n - i):
                matrix[x][y] = tmp[p]
                p += 1; x += 1
        return matrix