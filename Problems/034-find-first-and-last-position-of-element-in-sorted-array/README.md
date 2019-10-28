# [34. Search for a Range](https://leetcode.com/problems/search-for-a-range/)

## 题目

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

## 解题思路

使用两次二分查找，第一次找到最左边 `target` 的下标，所以在找到第一个 `target` 后不能马上停止，我们要继续搜索，直到 `left == right` 且它们在某个 `target` 值处下标相同
`flag` 参数的引入，它是一个 `bool` 类型的变量，指示在遇到 `target == nums[mid]` 时应该做什么。如果 `flag` 为 `true`，那么它们递归左区间，否则递归右区间。考虑如果我们在下标为 `i` 处遇到了 `target` ，最左边的 `target` 一定不会出现在下标大于 `i` 的位置，所以我们永远不需要考虑右子区间。当求最右下标时，道理同样适用。

详见代码

## 总结
