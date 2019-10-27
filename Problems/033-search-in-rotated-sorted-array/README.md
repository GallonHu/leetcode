# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## 题目

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

## 解题思路

注意到原数组为有限制的有序数组（除了在某个点会突然下降外均为升序数组）

1. `if nums[0] <= nums[i]` 那么 `nums[0]` 到 `nums[i]` 为有序数组, 那么当 `nums[0] <= target <= nums[i]` 时我们应该在 0-i0−i 范围内查找；

2. `if nums[i] < nums[0]` 那么在 `0-i` 区间的某个点处发生了下降（旋转），那么 `i+1` 到最后一个数字的区间为有序数组，并且所有的数字都是小于 `nums[0]` 且大于 `nums[i]`，当 `target` 不属于 `nums[0]` 到 `nums[i]` 时（`target <= nums[i] < nums[0]` or `nums[i] < nums[0] <= target`），我们应该在 `0-i` 区间内查找。
3. 上述三种情况可以总结如下：

    ```python
        nums[0] <= target <= nums[i]
                target <= nums[i] < nums[0]
                            nums[i] < nums[0] <= target
    ```

## 总结

本题是二分查找法的升级版
