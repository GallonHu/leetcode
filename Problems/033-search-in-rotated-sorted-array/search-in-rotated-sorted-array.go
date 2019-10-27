package problem033

func search(nums []int, target int) int {
	low, high := 0, len(nums)-1
	for low <= high {
		mid := (low + high) >> 1
		if target == nums[mid] {
			return mid
		} else if nums[mid] < nums[high] {
			if nums[mid] < target && target <= nums[high] {
				low = mid + 1
			} else {
				high = mid - 1
			}
		} else {
			if nums[low] <= target && target < nums[mid] {
				high = mid - 1
			} else {
				low = mid + 1
			}
		}
	}
	return -1
}
