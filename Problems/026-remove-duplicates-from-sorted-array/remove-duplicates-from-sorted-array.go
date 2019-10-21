package problem026

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	j := 1

	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			nums[j] = nums[i]
			j++
		}
	}

	return j
}
