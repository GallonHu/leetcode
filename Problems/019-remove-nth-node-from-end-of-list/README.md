# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## 题目

Given a linked list, remove the nth node from the end of list and return its head.

For example,

```
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
```

**Note**:

1. Given n will always be valid. 不存在链的长度<n的情况
1. Try to do this in one pass.

## 解题思路

### 快慢指针

1. 增加一个新节点, 其next指向head
2. 初始快慢节点均指向新节点
3. 快节点向前移动n个
4. 再同时移动快慢节点，则当快节点指向空时，慢节点指向倒数第n个节点的父节点
5. 将慢指针的next指向next的next
6. 返回新节点的next
