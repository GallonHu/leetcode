package problem001

func twoSum(nums []int, target int) []int {
	index := make(map[int]int, len(nums))

	for ind, val := range nums {
		index[val] = ind
	}

	for ind1, val := range nums {
		if ind2, ok := index[target-val]; ok {
			if ind2 != ind1 {
				return []int{ind1, ind2}
			}
		}
	}

	return nil
}
