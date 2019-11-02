# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

## 题目

Given an array of strings, group anagrams together.

```
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

## 解题思路

构建一个 hash 表，键为单词的 hash 表示，值为一个数组
返回所有的值即可
重点在如何构建键
详见代码

### 注意

hash 表的键只能为不可改变的数据！！！！

## 总结
