class Solution:
    def __init__(self):
            self.count = 0

    def totalNQueens(self, n: int) -> int:
        def backtrack(r=0):
            if r == n:
                self.count += 1
                return

            for c in range(n):
                id1 = c - r + n
                id2 = 2 * n - c - r - 1
                if not col[c] and not d1[id1] and not d2[id2]:
                    col[c], d1[id1], d2[id2] = True, True, True
                    backtrack(r + 1)
                    col[c], d1[id1], d2[id2] = False, False, False

        col = [False] * n
        d1 = [False] * 2 * n
        d2 = [False] * 2 * n
        backtrack()

        return self.count


print(Solution().totalNQueens(4))