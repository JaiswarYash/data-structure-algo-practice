class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = ''

        for char in s.lower():
            if char.isalnum():
                res += char
                
        left = 0
        right = len(res)-1

        while left < right:
            if res[left] != res[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
