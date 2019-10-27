class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        res = 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if i > 0 and s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif s[i-1] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                res = max(dp[i], res)
        
        return res