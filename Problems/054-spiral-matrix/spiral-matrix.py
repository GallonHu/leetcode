class Solution:
    # def spiralOrder(self, matrix):
    #     if not matrix:
    #         return []

    #     res = []
    #     m, n = len(matrix), len(matrix[0])
    #     less = min(m, n)

    #     for c in range(less // 2):
    #         for j in range(c, n - c):
    #             res.append(matrix[c][j])
    #         for i in range(c + 1, m - c - 1):
    #             res.append(matrix[i][n - c - 1])
    #         for j in range(c, n - c)[::-1]:
    #             res.append(matrix[m - c - 1][j])
    #         for i in range(c + 1, m - c - 1)[::-1]:
    #             res.append(matrix[i][c])
    #     if less % 2 == 1:
    #         if m < n:
    #             for j in range(less//2, n-less//2):
    #                 res.append(matrix[less//2][j])
    #         else:
    #             for i in range(less//2, m-less//2):
    #                 res.append(matrix[i][less//2])

    #     return res

    def spiralOrder(self, matrix):
        if not matrix:
            return []

        res = []
        m, n = len(matrix), len(matrix[0])
        top, down = 0, m - 1
        left, right = 0, n - 1
        x, y = 0, -1
        dx, dy = 0, 1

        for _ in range(m * n):
            x += dx
            y += dy
            if x + dx < top:
                left += 1
                dx, dy = 0, 1
            elif y + dy > right:
                top += 1
                dx, dy = 1, 0
            elif x + dx > down:
                right -= 1
                dx, dy = 0, -1
            elif y + dy < left:
                down -= 1
                dx, dy = -1, 0
            res.append(matrix[x][y])
        return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(matrix))