class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1]*len(nums)

        # left pass
        left = 1
        for i in range(len(nums)):
            ans[i] *= left
            left *= nums[i]
        # ouput of pass one -> [1,1,2,6]

        # right pass
        right = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= right
            right *= nums[i]
        return ans

