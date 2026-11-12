class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for i in strs:
            key = "".join(sorted(i))
            if key in anagrams:
                anagrams[key].append(i)
            else:
                anagrams[key] = []
                anagrams[key].append(i)
        return list(anagrams.values())

