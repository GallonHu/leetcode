package problem003

func lengthOfLongestSubstring(s string) int {
	index := [128]int{}
	for i := range index {
		index[i] = -1
	}

	ans, left := 0, 0

	for i := 0; i < len(s); i++ {
		if index[s[i]] >= left {
			left = index[s[i]] + 1

		} else if i-left+1 > ans {
			ans = i - left + 1
		}
		index[s[i]] = i
	}
	return ans
}
