class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq_count = {}

        for char in s:
            if char not in freq_count:
                freq_count[char] = 1
            else:
                freq_count[char] += 1
        
        for char in t:
            if char not in freq_count or freq_count[char] == 0:
                return False
            else:
                freq_count[char] -= 1
        return True


        