class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix) / 2):
                matrix[i][j], matrix[i][len(matrix) - 1 - j] = matrix[i][len(matrix) - 1 - j], matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix) - i - 1):
                matrix[i][j], matrix[len(matrix) - 1 - j][len(matrix) - 1 - i] = matrix[len(matrix) - 1 - j][
                                                                                     len(matrix) - 1 - i], matrix[i][j]
