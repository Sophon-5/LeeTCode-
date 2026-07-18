class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return - 1
        
        
        p = list(range(n))
        r = [0] * n
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x]) 
            return p[x]
            
        def union(x, y):
            xp = find(x)
            yp = find(y)
            if xp == yp:
                return False
           
            if r[xp] < r[yp]:
                p[xp] = yp
            elif r[xp] > r[yp]:
                p[yp] = xp
            else:
                p[xp] = yp
                r[yp] += 1
            return True

      
        components = n
        
        for u, v in connections:
            if union(u, v):
                components -= 1
                
        
        return components - 1