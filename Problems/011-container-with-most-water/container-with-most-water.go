package problem011

func maxArea(height []int) int {
	area, temp := 0, 0
	i, j := 0, len(height)-1

	for i < j {
		if height[i] < height[j] {
			temp = height[i] * (j - i)
			i++
		} else {
			temp = height[j] * (j - i)
			j--
		}

		if temp > area {
			area = temp
		}
	}

	return area
}
