# [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

## 题目

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character `'.'`.

You may assume that there will be only one unique solution.

![problem](1.png)

A sudoku puzzle...

![solution](2.png)

...and its solution numbers marked in red.

## 解题思路

1. 用三个二维 bool 数组分别记录记录每行、每列、每个 block 中各个数字是否存在
2. 先遍历 board，初始化 三个数组
3. 依此遍历 board 的第 count 个位置
   - 若当前位置为 '.'，依此判断 ['1' ……, '9'] 是否能放入当前位置
       - 若能，更新记录数组，继续遍历 board，直至最后一个位置，结束程序
       - 若不能，回溯
   - 若当前位置不为 '.'，遍历到下一个 board 位置

具体过程和细节，见程序及注释。

## 总结
