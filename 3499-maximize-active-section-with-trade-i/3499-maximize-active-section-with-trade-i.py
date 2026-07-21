class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ans = s.count('1')
        active = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                active.append(i-start)

            else:
                i += 1

        maxpairsum = 0
        for i in range(1,len(active)):
            maxpairsum = max(maxpairsum, active[i] + active[i-1])

        return maxpairsum + ans