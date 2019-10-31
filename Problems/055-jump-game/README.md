# [55. Jump Game](https://leetcode.com/problems/jump-game/)

## 题目

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position. 

Determine if you are able to reach the last index.

```
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
```

## 解题思路

关键能不能跨过数值为0的元素。

使用一个变量记录当前能到达的最远位置
核心公式为：far = max(i + nums[i], far)
最后判断：far >= len(nums)-1

见程序注释
