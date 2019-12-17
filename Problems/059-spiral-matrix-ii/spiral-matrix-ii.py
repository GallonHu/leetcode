#!/usr/bin/env python
# coding=utf-8
'''
@Author: Gallon
@Date: 2019-12-17 09:38:45
@LastEditTime: 2019-12-17 10:31:15
@FilePath: /leetcode/leetcode/Problems/059-spiral-matrix-ii/spiral-matrix-ii.py
'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]

        # 四周边界值
        t, b, l, r = 0, n-1, 0, n-1
        # 当前指针
        row, col = 0, -1
        # 方向
        r_step, c_step = 0, 1
        for i in range(1, n*n+1):
            row += r_step
            col += c_step
            res[row][col] = i

            # 超出右边界，将指针移到正确位置，上边界向下移动，同时改变方向
            if col+c_step > r:
                t += 1
                r_step, c_step = 1, 0
            # 超出下边界，将指针移到正确位置，右边界向左移动，同时改变方向
            if row+r_step > b:
                r -= 1
                r_step, c_step = 0, -1
            # 超出左边界，将指针移到正确位置，下边界向上移动，同时改变方向
            if col+c_step < l:
                b -= 1
                r_step, c_step = -1, 0
            # 超出上边界，将指针移到正确位置，左边界向右移动，同时改变方向
            if row+r_step < t:
                l += 1
                r_step, c_step = 0, 1

        return res