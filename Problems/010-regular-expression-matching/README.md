# [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

## 题目

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
Implement regular expression matching with support for '.' and '*'.

```text
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```

The matching should cover the entire input string (not partial).

Note:

- s could be empty and contains only lowercase letters a-z.
- p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

```text
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

Example 2:

```text
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

Example 3:

```text
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

Example 4:

```text
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
```

Example 5:

```text
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```

## 解题思路

按照动态规划的标准流程解题。

- 状态定义：
  - 设动态规划网格 dp ，dp[i][j] 代表字符串 s[:i] 和 p[:j] 是否匹配，值为 true 或 false 。
  - 记 s 和 p 长度分别为 sSize , pSize 。
- 初始状态：
  - dp[0][0] = true
  - 初始化第一行 j: 1->pSize : dp[0][j+1] = dp[0][j-1] and p[j] == '*'；
- 转移方程：
  - 当第 p[j] 和 s[i] 匹配时：
    - 只要前面匹配，这里就能匹配上: d[i+1][j+1] = d[i][j]
  - 否则
    - 当 p[j] == '*' 时
      - p[j] 无法与 s[i] 匹配上, p[j-1:j+1] 只能被当做 "": p[i+1][j+1] = p[i+1][j-1]
      - p[j] 与 s[i] 匹配上, p[j-1:j+1] 作为 "x*", 可以有三种解释: ""、"x"、"xx...":
        dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j] or dp[i][j+1]
- 返回值：
  - 字符串 s 中前 sSize 个字符和 p 中前 pSize 个字符是否匹配，即：dp[sSize][pSize]
