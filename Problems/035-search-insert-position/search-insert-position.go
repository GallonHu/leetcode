package problem035

func searchInsert(nums []int, target int) int {
	left, right := 0, len(nums)
	var mid int
	for left < right {
		mid = (left + right) >> 1
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return left
}
