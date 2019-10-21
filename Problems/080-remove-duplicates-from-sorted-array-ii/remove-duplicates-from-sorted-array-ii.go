package problem080

func removeDuplicates(nums []int) int {
	if len(nums) <= 2 {
		return len(nums)
	}
	idx := 1
	for i := 2; i < len(nums); i++ {
		if nums[i] != nums[idx-1] {
			idx++
			nums[idx] = nums[i]
		}
	}
	return idx + 1
}
