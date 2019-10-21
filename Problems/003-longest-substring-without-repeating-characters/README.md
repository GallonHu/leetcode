# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 题目

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

## 解题思路

使用滑动窗口，使用一个hash_map记录当前字母c在左边最近的位置，遍历字符串，若当前字母c在前面未出现过，窗口长度加1，若出现过，则更新窗口左边位置为hash_map[c]+1，再计算窗口长度。遍历完成，返回最大的窗口长度即可。

## 总结

利用Location保存字符上次出现的序列号，避免了查询工作。location和[Two Sum](../001-two-sum/README.md)中的m是一样的作用。

```go
// m 负责保存map[整数]整数的序列号
m := make(map[int]int, len(nums))
```
