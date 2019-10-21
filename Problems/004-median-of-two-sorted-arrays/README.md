# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## 题目

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

```
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
```

Example 2:

```
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
```

## 解题思路

使用二分查找
两个有序数组中找到第k大的数通用算法:

```
A: A_left A[m/2] A_right
B: B_left B[n/2] A_right
if A[m/2]>B[n/2] and k>m/2+n/2, then disregard B_left and B[n/2]
if A[m/2]>B[n/2] and k<=m/2+n/2, then disregard A_right and A[m/2]
if A[m/2]<=B[n/2] and k>m/2+n/2, then disregard A_left and A[m/2]
if A[m/2]<=B[n/2] and k<=m/2+n/2, then disregard B_right and B[n/2]
```

使用递归实现较为简单，详见代码

## 总结
