class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merge = [] # 

        for a,b in zip(word1, word2):
            merge.append(a + b)
        merge.append(word1[len(word2):])
        merge.append(word2[len(word1):])
        return ''.join(merge)

# Step 1: Zip pairs characters up to the shorter word's length
# e.g., "ab" + "pqrs" → pairs: ('a','p'), ('b','q')
# After loop: merge = ["ap", "bq"]

# Step 2: Append remaining characters from word1
# word1[4:] → "" (word1 is only 2 chars, nothing left)

# Step 3: Append remaining characters from word2
# word2[2:] → "rs"

# Step 4: Join everything into one string
# "ap" + "bq" + "" + "rs" = "apbqrs"