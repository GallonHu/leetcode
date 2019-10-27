# [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

## 题目

Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

For `"(()"`, the longest valid parentheses substring is `"()"`, which has length = 2.

Another example is `")()())"`, where the longest valid parentheses substring is `"()()"`, which has length = 4.

## 解题思路

动态规划

- 我们用 dp[i] 表示以 i 结尾的最长有效括号；

- 当s[i] 为 (, dp[i] 必然等于0, 因为不可能组成有效的括号;

- 那么s[i] 为 )

  1. 当 s[i-1] 为 (，那么 dp[i] = dp[i-2] + 2

  2. 当 s[i-1] 为 ) 并且 s[i-dp[i-1] - 1] 为 (，那么 dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]。

    注：这背后的原因是如果倒数第二个 `)` 是一个有效子字符串的一部分（记为 `sub_s`），对于最后一个 `)` ，如果它是一个更长子字符串的一部分，那么它一定有一个对应的 `(` ，它的位置在倒数第二个 `)` 所在的有效子字符串的前面（也就是 `sub_s` 的前面）。因此，如果子字符串 `sub_s` 的前面恰好是 `(` ，那么我们就用 2 加上 `sub_s` 的长度（dp[i-1]）去更新 dp[i]。除此以外，我们也会把有效子字符串 `"(,sub_s,)"` 之前的有效子字符串的长度也加上，也就是加上 dp[i-dp[i-1]-2] 。)

## 总结
