class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0]*n
        adj = [[] for _ in range(n)]

        for  i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)


        safe = [False]*n

        while q:
            node = q.popleft()
            safe[node] = True

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        safenodes = []
        for i in range(n):
            if safe[i]:
                safenodes.append(i)
        return safenodes