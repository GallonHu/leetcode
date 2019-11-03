class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.pow(x, -n)
        return self.pow(x, n)

    def pow(self, x: float, n: int):
        if n == 0: return 1
        if x == 0: return 0

        res = self.pow(x, n >> 1)
        while n & 1 == 0:
            return res * res
        return res * res * x


print(Solution().myPow(1, 10))