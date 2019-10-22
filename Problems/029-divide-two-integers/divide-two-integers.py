class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        count = 0
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        res = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                res += 1 << count
                dividend -= divisor

        if sign: res = -res
        return res if -(1 << 31) <= res <= (1 << 31) - 1 else (1 << 31) - 1