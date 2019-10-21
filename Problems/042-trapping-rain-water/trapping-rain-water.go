package problem042

func max(i, j int) int {
	if i >= j {
		return i
	}
	return j
}

func min(i, j int) int {
	if i >= j {
		return j
	}
	return i
}

// 动态规划
func trap1(height []int) int {
	if len(height) < 3 {
		return 0
	}

	n := len(height)
	left, right := make([]int, n), make([]int, n)
	ans := 0

	left[0], right[n-1] = height[0], height[n-1]
	for i := 1; i < n; i++ {
		left[i] = max(left[i-1], height[i])
		right[n-1-i] = max(right[n-i], height[n-1-i])

		// left[i] 是 height[:i+1] 中的最大值
		// right[i] 是 height[i:] 中的最大值
	}

	for i := 1; i < n-1; i++ {
		ans += min(left[i], right[i]) - height[i]
	}

	return ans
}

// 双指针
func trap2(height []int) int {
	if len(height) < 3 {
		return 0
	}

	lMax, rMax := 0, 0
	left, right := 0, len(height)-1
	ans := 0

	for left < right {
		if height[left] < height[right] {
			lMax = max(lMax, height[left])
			ans += lMax - height[left]
			left++
		} else {
			rMax = max(rMax, height[right])
			ans += rMax - height[right]
			right--
		}
	}

	return ans
}
