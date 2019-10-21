class Solution:
    def myAtoi(self, str: str) -> int:
        return self.convert(self.clean(str))

    def clean(self, s: str) -> (int, str):
        s = s.strip()
        if not s:
            return
        
        if s[0].isdigit():
            sign, num = 1, s
        elif s[0] == '+':
            sign, num = 1, s[1:]
        elif s[0] == '-':
            sign, num = -1, s[1:]
        else:
            return 1, ""
        
        for i, b in enumerate(num):
            if b < '0' or '9' < b:
                num = num[:i]
                break
        
        return sign, num

    def convert(self, param) -> int:
        if not param:
            return 0
        sign, num_str = param
        num = 0

        for b in num_str:
            num = num*10 + int(b)
            if sign == 1 and num >= 2**31:
                return 2**31 - 1
            elif sign == -1 and sign*num < -2**31:
                return -2**31
        
        return sign * num

print(Solution().myAtoi("-91283472332"))