class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = [-1] * 127
        ans = 0
        length = 0
        start = 0
        for i, c in enumerate(s):
            length += 1
            j = ord(c)
            if indices[j] >= start:
                length = i - indices[j]
                start = indices[j] + 1
            indices[j] = i
            if length > ans:
                ans = length
        return ans