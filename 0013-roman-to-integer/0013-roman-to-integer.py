class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman_to_int = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        for i in range(len(s)):
            # i+1 < len(s), <- part, Check if there is a next character exit or not
            if i+1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                res -= roman_to_int[s[i]]
            else:
                res += roman_to_int[s[i]]
        return res
#  Step 1: Create a map of Roman symbols → Values
# Step 2: Loop through each character (left → right)
# Step 3: Compare current value with next value, if Smaller before larger? → Subtract
# Otherwise? → Add
