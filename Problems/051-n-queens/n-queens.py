class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(r, board):
            if r == n:
                res.append(board+[])
                return
            
            for c in range(n):
                # 主对角
                id1 =  r - c + n
                # 次对角
                id2 = 2*n - r - c - 1 

                if not col[c] and not d1[id1] and not d2[id2]:
                    col[c], d1[id1], d2[id2] = True, True, True
                    backtrack(r+1, board+['.'*c+'Q'+'.'*(n-c-1)])
                    col[c], d1[id1], d2[id2] = False, False, False
        
        res = []
        col = [False] * n
        d1 = [False] * 2*n
        d2 = [False] * 2*n

        backtrack(0, [])

        return res