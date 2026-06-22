class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        dirs = [(0,-1), (0,1), (1,0), (-1,0)]
        mins = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in dirs:
                    newr = r + dr
                    newc = c + dc
                    if 0 <= newr < m and 0 <= newc < n and grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        q.append((newr,newc))
                        fresh -= 1
            mins += 1
        if fresh == 0:
            return mins
        else:
            return -1