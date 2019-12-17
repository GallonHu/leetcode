# [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

## 题目

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

**Note**: A word is defined as a character sequence consists of non-space characters only.

```
For example,
Given s = "Hello World",
return 5.
```

## 解题思路

先去除字符串两边的空格：如果为空，直接返回0；否则，以空格分割字符串，返回最后一个元素的长度。