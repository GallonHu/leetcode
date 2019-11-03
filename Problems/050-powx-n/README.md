# [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)

## 题目

Implement pow(x, n).

## 解题思路

注意到指数是整数，所以，使用二分法计算幂
核心公式：
$$
x^n = x^{(n/2)^2}
$$

## 总结

o(N)的算法会浪费很多时间，o(lgN)的算法要快的多。
