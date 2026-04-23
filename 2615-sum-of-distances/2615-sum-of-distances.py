class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        map = defaultdict(list)
        for i, num in enumerate(nums):
            map[num].append(i)
        res = [0] * len(nums)
        
        for indices in map.values():
            total_sum = sum(indices)
            left_sum = 0
            
            for i in range(len(indices)):
                idx = indices[i]
                
                count_left = i
                count_right = len(indices) - i - 1
                
                right_sum = total_sum - left_sum - idx
                
                # apply formula
                left_contribution = idx * count_left - left_sum
                right_contribution = right_sum - idx * count_right
                
                res[idx] = left_contribution + right_contribution
                
                # update prefix
                left_sum += idx

        return res