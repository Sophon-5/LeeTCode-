import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        mx = nums[-1]
        mn = nums[0]

        return math.gcd(mx,mn)