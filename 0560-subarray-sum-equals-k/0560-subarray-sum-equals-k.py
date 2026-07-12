class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        cnt = 0
        pref_sum = 0
        freq[0] = 1
        for i in range(len(nums)):
            pref_sum += nums[i]
            if (pref_sum - k) in freq:
                cnt  +=  freq[pref_sum - k]

            freq[pref_sum] += 1
        return cnt