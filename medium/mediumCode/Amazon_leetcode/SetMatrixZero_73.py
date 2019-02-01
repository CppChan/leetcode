class Solution(object):
    def setZeroes(self, matrix):
        fr, fc = False, False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and matrix[i][j] == 0: fr = True # pay attention
                if j == 0 and matrix[i][j] == 0: fc = True
                if matrix[i][j] == 0: matrix[i][0], matrix[0][j] = 0, 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
        if fr:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if fc:
            for i in range(len(matrix)):
                matrix[i][0] = 0
