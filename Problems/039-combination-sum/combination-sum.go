package problem039

import (
	"sort"
)

func combinationSum(candidates []int, target int) [][]int {
	var temp []int
	var res [][]int
	sort.Ints(candidates)
	backtrack(candidates, &res, temp, target, 0, len(candidates))

	return res
}

func backtrack(candidates []int, res *[][]int, temp []int, remain, start, end int) {
	if remain == 0 {
		*res = append(*res, temp)
		return
	} else if remain < 0 {
		return
	}

	// 这样处理一下的用意是，让切片的容量等于长度，以后append的时候，会分配新的底层数组
	// 避免多处同时对底层数组进行修改，产生错误的答案。
	// 可以注释掉以下语句，运行单元测试，查看错误发生
	temp = temp[:len(temp):len(temp)]
	for i := start; i < end; i++ {
		remain -= candidates[i]

		temp = append(temp, candidates[i])
		backtrack(candidates, res, temp, remain, i, end)
		remain += temp[len(temp)-1]
		temp = temp[:len(temp)-1]
	}
}
