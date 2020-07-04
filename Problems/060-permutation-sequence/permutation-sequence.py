#!/usr/bin/env python
# coding=utf-8
'''
@Author: Gallon
@Date: 2019-12-18 09:53:34
@LastEditTime: 2019-12-18 10:36:08
@FilePath: /leetcode/leetcode/Problems/060-permutation-sequence/permutation-sequence.py
'''

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = [str(i) for i in range(1, n+1)]
        res = ""
        n -= 1
        while n > -1:
            t = math.factorial(n)
            loc = math.ceil(k / t) - 1
            res += num[loc]
            num.pop(loc)
            k %= t
            n -= 1
        return res


print(Solution().getPermutation(3, 3))
