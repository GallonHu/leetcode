# [15. 3Sum](https://leetcode.com/problems/3sum/)

## 题目

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

```
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

## 解题思路

1. 先排序
2. 固定一个值i，再使用双指针i,j分别指向剩余部分的首位，判断三个指针出值之和是否为0，若为0，则是一个满足的解，j++, k--；若大于0，右指针j--；若小于0，左指针i++
3. 去重策略：若i与i--处的值相同，i++；若i处的值大于0，后面不肯能存在解，直接退出；若j与j-1处的值相同，i++；若k与k++处的值相同，k--
