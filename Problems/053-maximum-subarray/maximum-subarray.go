package problem053

func maxSubArray(nums []int) int {
	ans := nums[0]

	for i := 1; i < len(nums); i++ {
		nums[i] = nums[i] + max(0, nums[i-1])
		ans = max(ans, nums[i])
	}

	return ans
}

func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}
