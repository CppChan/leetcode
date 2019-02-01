class TicTacToe(object):

    def __init__(self, n):
        self.rows, self.cols, self.n = {}, {}, n
        for i in range(n):
            self.rows[i] = [-1, 0]
            self.cols[i] = [-1, 0]
        self.dig1 = [-1, 0]
        self.dig2 = [-1, 0]

    def move(self, row, col, player):
        row_pos = self.rows[row]
        col_pos = self.cols[col]
        if self.change(row_pos, player) == player: return player
        if self.change(col_pos, player) == player: return player
        if row == col and self.change(self.dig1, player) == player: return player
        if row + col + 1 == self.n and self.change(self.dig2, player) == player: return player
        return 0

    def change(self, array, player):
        if array[0] == -1 or array[0] == player:
            array[0] = player
            array[1] += 1
            if array[1] == self.n: return player
        else:
            array[0] = "*"
