package problem027

func removeElement(nums []int, val int) int {
	idx := 0

	for _, i := range nums {
		if i != val {
			nums[idx] = i
			idx++
		}
	}

	return idx
}
