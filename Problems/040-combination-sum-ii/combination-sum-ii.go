package problem040

import "sort"

func combinationSum2(candidates []int, target int) [][]int {
	var res [][]int

	sort.Ints(candidates)
	backtrack(candidates, target, 0, []int{}, &res)

	return res
}

func backtrack(candidates []int, target, start int, path []int, res *[][]int) {
	if target == 0 {
		*res = append(*res, path)
		return
	}

	for i := start; i < len(candidates); i++ {
		if i > start && candidates[i] == candidates[i-1] {
			continue
		}
		if target-candidates[i] < 0 {
			break
		}
		backtrack(candidates, target-candidates[i], i+1, append(path, candidates[i]), res)
	}
}
