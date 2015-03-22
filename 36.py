class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def valid(self, line):
        line.sort()
        for i in range(9):
            if line[i] == '.':
                continue
            if int(line[i]) < 1 or int(line[i]) > 9:
                return False
            if i < 8 and line[i] == line[i+1]:
                return False
        return True
            
    def isValidSudoku(self, board):
        for i in range(9):
            tmp = []; tmp2 = []
            for j in range(9):
                tmp.append(board[j][i])
                tmp2.append(board[i][j])
            if not self.valid(tmp) or not self.valid(tmp2):
                return False
        for i in range(3):
            for j in range(3):
                tmp = []
                for p in range(i * 3, i * 3 + 3):
                    for q in range(j * 3, j * 3 + 3):
                        tmp.append(board[p][q])
                if not self.valid(tmp):
                    return False
        return True