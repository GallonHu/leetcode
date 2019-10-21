import queue

class Cell:
    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.height = height
    
    def __lt__(self, other):
        return self.height < other.height

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        pq = queue.PriorityQueue()
        
        isVisited = [[False]*n for _ in range(m)]
        for i in range(m):
            isVisited[i][0] = True
            isVisited[i][n-1] = True
            pq.put(Cell(i, 0, heightMap[i][0]))
            pq.put(Cell(i, n-1, heightMap[i][n-1]))
        for j in range(n):
            isVisited[0][j] = True
            isVisited[m-1][j] = True
            pq.put(Cell(0, j, heightMap[0][j]))
            pq.put(Cell(m-1, j, heightMap[m-1][j]))
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        vol = 0

        while not pq.empty():
            c = pq.get()
            for d in dirs:
                i = c.row + d[0]
                j = c.col + d[1]

                if 0 <= i < m and 0 <= j < n and not isVisited[i][j]:
                    isVisited[i][j] = True
                    vol += max(0, c.height-heightMap[i][j])
                    pq.put(Cell(i, j, max(c.height, heightMap[i][j])))
                
        return vol
