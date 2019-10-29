package problem037

func solveSudoku(board [][]byte) {
	var appearInRow, appearInCol, appearInBlock [9][10]bool

	// 初始化 appearInRow, appearInCol, appearInBlock
	// 将出现数字的相应位置置 true
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if board[i][j] == '.' {
				continue
			}

			num := board[i][j] - '0'
			appearInRow[i][num] = true
			appearInCol[j][num] = true
			appearInBlock[i/3*3+j/3][num] = true
		}
	}

	// 开始遍历
	solve(board, 0, appearInRow, appearInCol, appearInBlock)
}

func solve(board [][]byte, count int, appearInRow, appearInCol, appearInBlock [9][10]bool) bool {
	if count == 81 {
		return true
	}

	row, col := count/9, count%9
	if board[row][col] != '.' {
		return solve(board, count+1, appearInRow, appearInCol, appearInBlock)
	}

	for b := byte('1'); b <= '9'; b++ {
		num := b - '0'
		if !appearInRow[row][num] && !appearInCol[col][num] && !appearInBlock[row/3*3+col/3][num] {
			board[row][col] = b
			appearInRow[row][num], appearInCol[col][num], appearInBlock[row/3*3+col/3][num] = true, true, true
			if solve(board, count+1, appearInRow, appearInCol, appearInBlock) {
				return true
			}
			// 回溯
			appearInRow[row][num], appearInCol[col][num], appearInBlock[row/3*3+col/3][num] = false, false, false
		}
	}

	board[row][col] = '.'

	return false
}
