# [47. Permutations II](https://leetcode.com/problems/permutations-ii/)

## 题目

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
`[1,1,2]` have the following unique permutations:

```
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

## 解题思路

本题和[46. Permutations](https://leetcode.com/problems/permutations/)的区别在于，存在重复的数字。
先排序，方便后续剪枝
剪枝操作详见代码

## 总结
