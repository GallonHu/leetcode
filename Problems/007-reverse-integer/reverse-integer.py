class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = -x

        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10

        if -2**31 <= res < 2**31:
            return flag * res
        return 0
