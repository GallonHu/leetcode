# [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

## 题目

Given an unsorted integer array, find the first missing positive integer.

For example,

```
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
```

Your algorithm should run in O(n) time and uses constant space.

## 解题思路

1. 整理 nums ，让 nums[k] == k+1，只要 k+1 存在于 nums 中
2. 循环结束后，所有 1<=k+1<=len(nums) 且 k+1 存在于nums中，都会被存放于 nums[k] 中
3. 整理后，第一个不存在的 k+1 就是答案

注意：nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] 在 python中 这样交换的话，先计算右边的值，然后将右边第一个值赋值给左边第一个值（nums[i]=nums[nums[i]-1]），赋值完成后将右边第二个值赋值给左边第二个值（nums[nums[i]-1] = nums[i]），此时 nums[nums[i]-1] 中的 nums[i] 使用的是前一步的结果，故结果发生错误！！！！！！！

## 总结

注意到返回值只可能在 [1, n+1]（左闭右闭）区间内
