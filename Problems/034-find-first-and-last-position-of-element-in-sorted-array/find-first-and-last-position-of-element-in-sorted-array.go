package problem034

func searchRange(nums []int, target int) []int {
	leftIdx := binarrySearch(nums, target, true)

	if leftIdx == len(nums) || nums[leftIdx] != target {
		return []int{-1, -1}
	}

	return []int{leftIdx, binarrySearch(nums, target, false) - 1}
}

func binarrySearch(nums []int, target int, flag bool) int {
	left, right := 0, len(nums)
	var mid int
	for left < right {
		mid = (left + right) >> 1
		if nums[mid] > target || (flag && nums[mid] == target) {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return left
}
