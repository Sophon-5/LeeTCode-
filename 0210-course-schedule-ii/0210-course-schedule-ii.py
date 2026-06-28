class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [False] * numCourses
        pathvisited = [False] * numCourses
        st = []

        adj =[[]for _ in range(numCourses)]
        for course,pre in prerequisites:
            adj[pre].append(course)
        
        
        def dfs(node):
            visited[node] = True
            pathvisited[node] = True

            for neigh in adj[node]:
                if not visited[neigh]:
                    if dfs(neigh):
                        return True
                elif pathvisited[neigh]:
                    return True
                    

            pathvisited[node] = False
            st.append(node)
            return False


        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return []
        return st[::-1]