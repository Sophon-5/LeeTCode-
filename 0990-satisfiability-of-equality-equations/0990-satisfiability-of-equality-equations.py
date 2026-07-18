class Solution:
    def find(self,i, parent):
        if i == parent[i]:
            return i
        parent[i] = self.find(parent[i], parent)
        return parent[i]

    def union(self,x,y,parent,rank):
        x_par = self.find(x,parent)
        y_par = self.find(y,parent)
        if x_par == y_par:
            return False
        if rank[x_par] > rank[y_par]:
            parent[y_par] = x_par
        elif rank[x_par] < rank[y_par]:
            parent[x_par] = y_par
        else:
            parent[x_par] = y_par
            rank[y_par] += 1
        return True
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]

        rank = [0]*26
        for s in equations:
            if s[1]=='=' : 
                first = ord(s[0]) - ord('a')
                second = ord(s[3]) - ord('a')
                self.union(first,second,parent,rank)

        for s in equations:
            if s[1]=='!':
                first = ord(s[0]) - ord('a')
                second = ord(s[3]) - ord('a')

                f_p = self.find(first, parent)
                s_p = self.find(second, parent)
                if f_p==s_p:
                    return False
        return True