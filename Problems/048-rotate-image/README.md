# [48. Rotate Image](https://leetcode.com/problems/rotate-image/)

## 题目

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

## 解题思路

对应的4个点，依次互换位置。
(i, j) > (j, n-i-1)
(j, n-i-1) > (n-i-1, n-j-1)
(n-i-1, n-j-1) > (n-j-1, i)
(n-j-1, i) > (i, j)

## 总结
