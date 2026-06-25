class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # create hasmap :- seen 
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
        