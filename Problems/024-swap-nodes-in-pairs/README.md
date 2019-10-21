# [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

## 题目

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

## 解题思路

先添加一个空头再进行交换，比如a-b-c-d，
比如交换a-b时，前面加了空头，tmp-a-b-c-d,交换的步骤如下

1. tmp.next=b
2. a.next=c
3. b.next=a
此时为：tmp-b-a-c-d
下一步交换c-d时，因为c-d交换后，a.next也要变，所以下一步就把a当作c-d的头
4. tmp=tmp.next.next(即a)
tmp-c-d重复上面的步骤1-2-3步骤

## 总结
