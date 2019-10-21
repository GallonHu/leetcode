class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                res += i[0]
                continue
            break
        
        return res