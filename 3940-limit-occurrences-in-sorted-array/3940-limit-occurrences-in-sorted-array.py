from collections import defaultdict
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []
        freq= defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1
            if freq[nums[i]] <= k:
                res.append(nums[i])

        return res