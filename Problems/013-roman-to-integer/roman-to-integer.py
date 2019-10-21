class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        res, last = 0, 0
        for i in range(len(s))[::-1]:
            temp = d[s[i]]

            sign = 1
            if temp < last:
                sign = -1
            
            res += sign*temp
            
            last = temp
        
        return res