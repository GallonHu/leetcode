# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## 题目

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`,

the contiguous subarray `[4,-1,2,1]` has the largest sum = `6`.

More practice:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## 解题思路

使用动态规划，核心迭代公式为
$$
nums[i] = nums[i] + max(0, nums[i-1])
$$
