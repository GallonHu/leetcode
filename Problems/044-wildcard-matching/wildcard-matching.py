class Solution:
    def isMatch1(self, s, p):
        """
        双指针
        """
        i = 0
        j = 0
        start = -1
        match = 0
        while i < len(s):
            # 一对一匹配,匹配成功一起移
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            # 记录p的"*"的位置,还有s的位置
            elif j < len(p) and p[j] == "*":
                start = j
                match = i
                j += 1
            # j 回到 记录的下一个位置
            # match 更新下一个位置
            # 这不代表用*匹配一个字符
            elif start != -1:
                j = start + 1
                match += 1
                i = match
            else:
                return False
        # 将多余的 * 直接匹配空串
        return all(x == "*" for x in p[j:])

    def isMatch2(self, s: str, p: str) -> bool:
        """
        动态规划
        """
        sSize, pSize = len(s), len(p)
        dp = [[False for _ in range(pSize + 1)] for _ in range(sSize + 1)]

        dp[0][0] = True
        for j in range(1, pSize + 1):   
            dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'

        for i in range(1, sSize + 1):
            for j in range(1, pSize + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1]
                                                     or p[j - 1] == '?')
                else:
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[-1][-1]


Solution().isMatch2("acdcb", "a*c?b")