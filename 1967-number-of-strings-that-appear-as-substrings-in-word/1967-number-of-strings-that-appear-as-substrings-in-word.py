class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt  = 0
        for chars in patterns:
            if chars in word:
                cnt += 1

        return cnt