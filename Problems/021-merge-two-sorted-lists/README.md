# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## 题目

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

## 解题思路

把两个排序好的链合并，要求合并后依然是排序好的。结题步骤如下：

1. 新建一个节点, 采用二分排序算法中合并的步骤依此将节点加到新节点的后面
2. 返回新节点的下一个节点 

## 总结

合理地安排步骤，可以有效地减轻后面的判断条件和处理步骤，让整个函数更清晰易懂。
