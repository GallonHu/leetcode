# [46. Permutations](https://leetcode.com/problems/permutations/)

## 题目

Given a collection of distinct numbers, return all possible permutations.

For example,
`[1,2,3]` have the following permutations:

```
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## 解题思路

使用回溯算法，每次将添加如 temp 的数从 nums 中删除。当 nums 为空时，temp 即为一个合理的组合序列。
详见代码

### 注意

特别注意 slice 在 go 语言中的底层实现以及相关赋值操作

## 总结
