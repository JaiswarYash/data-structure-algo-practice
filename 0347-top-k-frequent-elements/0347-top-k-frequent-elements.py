class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        while len(hashmap) > k:

            min_key = min(hashmap, key=hashmap.get)
            del hashmap[min_key]

        return list(hashmap.keys())
        