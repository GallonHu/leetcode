package problem036

func isValidSudoku(board [][]byte) bool {
	dicRow := make([]map[byte]int, 9)
	dicCol := make([]map[byte]int, 9)
	dicBox := make([]map[byte]int, 9)
	for i := 0; i < 9; i++ {
		dicRow[i] = make(map[byte]int)
		dicCol[i] = make(map[byte]int)
		dicBox[i] = make(map[byte]int)
	}

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			c := board[i][j]
			if c == '.' {
				continue
			}
			_, ok1 := dicRow[i][c]
			_, ok2 := dicCol[j][c]
			_, ok3 := dicBox[3*(i/3)+j/3][c]
			if !ok1 && !ok2 && !ok3 {
				dicRow[i][c] = 1
				dicCol[j][c] = 1
				dicBox[3*(i/3)+j/3][c] = 1
			} else {
				return false
			}
		}
	}

	return true
}
