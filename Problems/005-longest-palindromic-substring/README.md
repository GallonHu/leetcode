# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

## 题目

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

Example:

```
Input: "cbbd"
Output: "bb"
```

## 解题思路

### 解法一 中心扩展：

从中心往两端扩展

1. 当l为奇数时，回文的`正中间段`只会是，“x”，或“xxx”，或“xxxxx”，或...
2. 当l为偶数时，回文的`正中间段`只会是，“xx”，或“xxxx”，或“xxxxxx”，或...
3. 同一个字符串的任意两个回文substring的`正中间段`，不会重叠。
4. 依此遍历每个中心段，返回最长回文即可

### 解法二 Manacher算法：

[参考](https://www.cnblogs.com/grandyang/p/4475985.html)
核心代码:
p[i] = mx > i ? min(p[2*id-1], mx-i): 1

## 总结

充分利用查找对象的特点，可以加快查找速度。
