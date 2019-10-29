# [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

## 题目

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

``` 
[
  [7],
  [2, 2, 3]
]
```

## 解题思路

回溯剪枝
将 candidates 先排序，方便后续剪枝

### 注意

- python: res.append(temp[:])
- go
  - temp = temp[:len(temp):len(temp)] append 长度和容量的变化对结果会有影响
  - 递归时应时候 res 的指针

### 关于递归的终结

1. 递归调用必须有终止条件。
2. 递归调用总是去尝试解决规模更小的子问题，这样递归才能收敛于终止条件。
3. 递归调用的子集必须是对父集的一个划分，不然，就会漏掉或者出现重复的结果。

## 总结
