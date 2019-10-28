# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

## 题目

Determine if a Sudoku is valid, according to: [Sudoku Puzzles - The Rules.](http://sudoku.com.au/TheRules.aspx)

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
![sudoku](sudoku.png)

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

## 解题思路

数独的规则很简单：

1. 横着的9个数，不能重复
1. 竖着的9个数，不能重复
1. 3×3小方块中的9个数，也不能重复

注意：对于 board[i][j] 元素，它在第 i 行，第 j 列，第 3*(i/3)+(j/3) 个 box 中
详见代码

## 总结
