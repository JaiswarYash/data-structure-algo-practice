class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create dict
        group = {}

        # using for loop
        for i in strs:
            key = ''.join(sorted(i))
            if key not in group:
                group[key] = []
                group[key].append(i)
            else:
                group[key].append(i)
        return list(group.values())


'''
Step 1: Loop through each word in the original list (don't sort the list).

Step 2: Sort the letters of the current word to get a key (like "eat" → "aet").

Step 3: Check if that key exists in the dictionary.

Step 4: If yes — append the original word to the list under that key.

Step 5: If no — create a new key with an empty list, then append the original word to it.

Step 6: Repeat Steps 2–5 for the next word in the original list.

Step 7: return the ans in list format
'''