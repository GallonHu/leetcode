class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0

        l = len(needle)
        for i in range(len(haystack)-l+1):
            if haystack[i: i+l] == needle:
                return i
        
        return -1

    def pythonic(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)