package problem057

func insert(intervals [][]int, newInterval []int) [][]int {
	lenA := len(intervals)

	if lenA == 0 {
		return [][]int{newInterval}
	}

	if newInterval[1] < intervals[0][0] {
		return append([][]int{newInterval}, intervals...)
	}

	if intervals[lenA-1][1] < newInterval[0] {
		return append(intervals, newInterval)
	}

	res := make([][]int, 0, len(intervals))
	for i := range intervals {
		if isOverlap(intervals[i], newInterval) {
			newInterval = merge(intervals[i], newInterval)

			if i == lenA-1 {
				res = append(res, newInterval)
			}

			continue
		}

		if intervals[i][1] < newInterval[0] {
			res = append(res, intervals[i])
			continue
		}

		if newInterval[1] < intervals[i][0] {
			res = append(res, newInterval)
			res = append(res, intervals[i:]...)
			break
		}

	}

	return res
}

func isOverlap(intervals, b []int) bool {
	return (intervals[0] <= b[0] && b[0] <= intervals[1]) || (intervals[0] <= b[1] && b[1] <= intervals[1]) || (b[0] <= intervals[0] && intervals[0] <= b[1])
}

func merge(intervals, b []int) []int {
	return []int{
		min(intervals[0], b[0]),
		max(intervals[1], b[1]),
	}
}

func min(intervals, b int) int {
	if intervals < b {
		return intervals
	}
	return b
}

func max(intervals, b int) int {
	if intervals > b {
		return intervals
	}
	return b
}
