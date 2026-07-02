class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        q = deque([(0,0)])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while  q:
            r,c = q.popleft()
            for dr,dc in dirs:
                nr , nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost= dist[r][c] + grid[nr][nc]

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost

                        if grid[nr][nc] == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))

        return dist[m-1][n-1] < health