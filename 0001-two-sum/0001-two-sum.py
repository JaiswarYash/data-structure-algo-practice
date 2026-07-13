class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [i, seen[compliment]]
            else:
                seen[num] = i
'''
1. to store each number and its index as we iterate.
2. Loop through nums with index i and value num.
3. compliment = target - num — the value we need to reach the target.
4. if compliment in seen — if we've already run into the needed complement, return its index and the current index.
5. seen[num] = i — otherwise, store the current number and its index for future lookups.
'''        