class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(nums):
            value = target - num
            if value in seen:
                return [i, seen[value]]
            else:
                seen[num] = i