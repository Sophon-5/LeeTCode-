class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj  = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visited[node] = True
            size = 1

            for nei in adj[node]:
                if not visited[nei]:
                    size += dfs(nei)
            return size

        visited = [False]*n
        remainingNodes = n
        res = 0
        for i in range(n):
            if not visited[i]:
                size  = dfs(i)
                
                res += size*(remainingNodes - size)
                remainingNodes -= size

        return res
