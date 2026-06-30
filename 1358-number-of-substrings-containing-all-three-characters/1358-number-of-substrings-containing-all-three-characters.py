class Solution:
    def numberOfSubstrings(self, s: str) -> int:
            freq ={
            'a' : 0,
            'b' : 0,
            'c' : 0
            }
            cnt = r = l = 0
            for r in range(len(s)):
                freq[s[r]] += 1
                while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                    cnt += (len(s) - r)
                    freq[s[l]] -= 1
                    l += 1

            return cnt
        