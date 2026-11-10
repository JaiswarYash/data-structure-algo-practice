class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) +1
        
        for char in t:
            if char in counts:
                counts[char] -= 1
                if counts[char] == 0:
                    del counts[char]
            else:
                counts[char] = counts.get(char,0)

            if len(counts) == 0:
                return True
        return False          