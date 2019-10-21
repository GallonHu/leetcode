class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sSize, pSize = len(s), len(p)
        dp = [[False for _ in range(pSize + 1)] for _ in range(sSize+1)]

        dp[0][0] = True
        for j in range(1, pSize, 2):
            dp[0][j+1] = dp[0][j-1] and p[j] == '*'

        for i in range(sSize):
            for j in range(pSize):
                if s[i] == p[j] or p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i +
                           1][j +
                              1] = dp[i + 1][j - 1] or dp[i +
                                                          1][j] or dp[i][j + 1]

        return dp[sSize][pSize]