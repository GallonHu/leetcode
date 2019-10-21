package problem044

func isMatch(s, p string) bool {
	sSize, pSize := len(s), len(p)

	dp := make([][]bool, sSize+1)
	for i := range dp {
		dp[i] = make([]bool, pSize+1)
	}

	dp[0][0] = true
	for j := 1; j <= pSize && dp[0][j-1]; j++ {
		if p[j-1] == '*' {
			dp[0][j] = true
		}
	}
}
