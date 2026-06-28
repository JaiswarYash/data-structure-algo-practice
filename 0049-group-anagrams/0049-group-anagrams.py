class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create dict
        bucket = {}

        # step 2 - lopp through list of str
        for i in strs:
            sorted_key = ''.join(sorted(i))

            if sorted_key in bucket:
                bucket[sorted_key].append(i)
            else:
                bucket[sorted_key] = []
                bucket[sorted_key].append(i)
        return list(bucket.values())

'''
Step 1: Loop through each word in the original list (don't sort the list).

Step 2: Sort the letters of the current word to get a key (like "eat" → "aet").

Step 3: Check if that key exists in the dictionary.

Step 4: If yes — append the original word to the list under that key.

Step 5: If no — create a new key with an empty list, then append the original word to it.

Step 6: Repeat Steps 2–5 for the next word in the original list.

Step 7: return the ans in list format
'''