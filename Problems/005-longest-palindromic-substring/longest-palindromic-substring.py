class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        中心扩展
        """
        if len(s) < 2:
            return s
        
        begin, maxLen = 0, 1

        i = 0
        while i < len(s)-1:
            if len(s)-i <= maxLen // 2:
                break

            b, e = i, i
            while e < len(s)-1 and s[e+1] == s[e]:
                e += 1

            i = e+1

            while e < len(s)-1 and b > 0 and s[e+1] == s[b-1]:
                b -= 1
                e += 1
            
            newLen = e+1-b
            if newLen > maxLen:
                begin = b
                maxLen = newLen
        
        return s[begin: begin+maxLen]

        def manacher(self, s: str) -> str:
            """
            Manacher算法
            """
            t = '#'.join(s)
            t = '$#' + t + '#^'

            p = [1] * len(t)
            mx, id, res_len, res_center = 0, 0, 0, 0
            for i in range(1, len(t)-1):
                if mx > i:
                    p[i] = min(p[2*id-i], mx-i)

                while t[i+p[i]] == t[i-p[i]]:
                    p[i] += 1
                
                if mx < i + p[i]:
                    mx = i+p[i]
                    id = i
                
                if res_len < p[i]:
                    res_len = p[i]
                    res_center = i
            
            return s[(res_center-res_len)//2: (res_center+res_len)//2-1]