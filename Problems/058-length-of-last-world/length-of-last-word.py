#!/usr/bin/env python
# coding=utf-8
'''
@Author: Gallon
@Date: 2019-12-17 09:23:58
@LastEditTime: 2019-12-17 09:28:33
@FilePath: /leetcode/leetcode/Problems/058-length-of-last-world/length-of-last-word.py
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        return len(s.split()[-1])