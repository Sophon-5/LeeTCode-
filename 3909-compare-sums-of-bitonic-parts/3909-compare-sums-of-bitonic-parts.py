class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        peak = 0
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                peak = i

        asc_sum = sum(nums[:peak+1])
        desc_sum = sum(nums[peak:len(nums)])

        if asc_sum > desc_sum:
            return 0
        elif asc_sum < desc_sum:
            return 1
        else:
            return -1