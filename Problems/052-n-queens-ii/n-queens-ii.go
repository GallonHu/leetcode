package problem052

func totalNQueens(n int) int {
	col := make([]bool, n)
	d1 := make([]bool, 2*n)
	d2 := make([]bool, 2*n)
	res := 0
	backtrack(&res, 0, n, col, d1, d2)

	return res
}

func backtrack(res *int, r, n int, col, d1, d2 []bool) {
	if r == n {
		*res++
		return
	}

	for c := 0; c < n; c++ {
		id1 := r - c + n
		id2 := 2*n - r - c - 1
		if !col[c] && !d1[id1] && !d2[id2] {
			col[c], d1[id1], d2[id2] = true, true, true
			backtrack(res, r+1, n, col, d1, d2)
			col[c], d1[id1], d2[id2] = false, false, false
		}
	}
}
