# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

## 题目

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

## 解题思路

### 解法一 堆

1. 建立一个大小为 lists 长度的堆
2. 初始将每个链表的头节点放入堆中
3. 当堆不为空时
4. 取堆的第一个节点加入结果链表中
5. 将取出的节点的下一个节点加入堆中
6. 循环直至堆空

### 解法二 归并

让lists中临近的list先两两合并，再让新生成的lists中的临近list两两合并，直到合并完成。

## 总结
