class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n = str(n)
        if n[0] != str(x) and str(x) in n:
            return True
        return False
     