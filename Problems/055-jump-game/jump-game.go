package problem055

func canJump(nums []int) bool {
	far := nums[0]
	for i := 1; i < len(nums)-1; i++ {
		if far < i {
			break
		}
		if i+nums[i] > far {
			far = i + nums[i]
		}
	}

	return far >= len(nums)-1
}
