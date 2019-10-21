class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s
            
        res = ''
        n = len(s)
        p = 2 * numRows - 2

        for i in range(0, n, p):
            res += s[i]

        for i in range(1, numRows - 1):
            res += s[i]

            for k in range(p, n + i, p):
                res += s[k - i]
                if k + i < n:
                    res += s[k + i]

        for i in range(numRows - 1, n, p):
            res += s[i]

        return res
