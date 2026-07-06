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

# visualization :
'''
1. ans = [1,1,1,1] <- size of nums

left pass :

2. left = 1, ans = [1,]

3. left = 1, nums[i] = 1 :- left*nums[i] = (1 * 1) :- ans = 1
ans = [1,1]

4. left = 1, nums[i] = 2 :- left*nums[i] = (1 * 2) :- ans = 2
ans = [1,1,2,]

5. left = 1, nums[i] = 3 :- left*nums[i] = (2 * 3) :- ans = 6
ans = [1,1,2,6]

here lenght of ans end so we stop

now right pass - ( starting from backword)

1. ans = [1,1,2,6]

2. right = 1, ans = [1,1,2,6 x 1] :- [1,1,2,6]

3. right = 1, nums[i] = 4 :- right*nums[i] = (1 * 4) = 4 :- ans = [1,1,2*4,6]
ans = [1,1,8,6]

3. right = 4, nums[i] = 3 :- right*nums[i] = (4 * 3) = 12 :- ans = [1,1*12,8,6]
ans = [1,12,8,6]

3. right = 12, nums[i] = 2 :- right*nums[i] = (12 * 2) = 24 :- ans = [1*24,12,8,6]
ans = [24,12,8,6]
'''