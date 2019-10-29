class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        appearInRow = [[False for _ in range(10)] for _ in range(9)]
        appearInCol = [[False for _ in range(10)] for _ in range(9)]
        appearInBlock = [[False for _ in range(10)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = ord(board[i][j]) - ord('0')
                appearInRow[i][num] = True
                appearInCol[j][num] = True
                appearInBlock[3 * (i // 3) + j // 3][num] = True

        self.solve(board, 0, appearInRow, appearInCol, appearInBlock)

    def solve(self, board, count, appearInRow, appearInCol, appearInBlock):
        if count == 81:
            return True

        row, col = count // 9, count % 9
        if board[row][col] != '.':
            return self.solve(board, count + 1, appearInRow, appearInCol,
                              appearInBlock)

        for b in range(1, 10):
            num = b
            b = str(b)
            if not appearInRow[row][num] and not appearInCol[col][
                    num] and not appearInBlock[row // 3 * 3 + col // 3][num]:
                board[row][col] = b
                appearInRow[row][num], appearInCol[col][num], appearInBlock[
                    row // 3 * 3 + col // 3][num] = True, True, True
                if self.solve(board, count + 1, appearInRow, appearInCol,
                              appearInBlock):
                    return True
                appearInRow[row][num], appearInCol[col][num], appearInBlock[
                    row // 3 * 3 + col // 3][num] = False, False, False

        board[row][col] = '.'

        return False


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
Solution().solveSudoku(board)
print(board)