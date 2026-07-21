class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0]*n
        right_sum = [0]*n
        for i in range(n):
            left_sum[i] += sum(nums[:i])
            right_sum[i] += sum(nums[i+1:])
        
        ans = []
        for i in range(n):
            ans.append(abs(left_sum[i] - right_sum[i]))

        return ans