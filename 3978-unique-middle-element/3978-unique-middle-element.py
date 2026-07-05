class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        mid = n // 2
        mid_elem = nums[mid]
        cnt = 0
        for i in range(n):
            if nums[i] == mid_elem:
                cnt += 1

        if cnt > 1:
            return False
        return True