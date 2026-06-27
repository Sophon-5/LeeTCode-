class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course,pre in prerequisites:
            adj[pre].append(course)

        vis = [False]*numCourses
        path = [False]*numCourses


        def dfs(node):
            vis[node] = path[node] = True
            for neigh in adj[node]:
                if not vis[neigh]:
                    if dfs(neigh):
                        return True
                elif path[neigh]:
                    return True

            path[node] = False
            return False

        for i in range(numCourses):
            if not vis[i]:
                if dfs(i):
                    return False

        return True
