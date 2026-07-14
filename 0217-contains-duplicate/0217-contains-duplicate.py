class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # create hasmap :- seen 
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# my solution
'''
1. created set with variable name seen. 
2. cuase, set() data structure which unordered and unique element and take no duplicates.
3. after each iteration, i will check if element exist in "seen".
4. if yes return True
5. if no return no
'''
        