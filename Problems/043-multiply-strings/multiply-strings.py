class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = list(map(lambda i: ord(i)-ord('0'), num1))
        num2 = list(map(lambda i: ord(i)-ord('0'), num2))
        l1, l2 = len(num1), len(num2)
        res = [0 for i in range(l1+l2-1)]
        
        for i in range(l1):
            for j in range(l2):
                res[i+j] += num1[i] * num2[j] 
        
        for i in range(1, len(res))[::-1]:
            res[i-1] += res[i] // 10
            res[i] = res[i] % 10

        return ''.join(map(str, res))
