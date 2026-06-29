class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create default dict
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1
            # counter[n] = 1 + counter.get(n, 0) -> use this line  instead of "counter[n] += 1"  if we are not using defaultdict()
        
        freq = [[] for _ in range(len(nums)+1)]

        for n, f in counter.items():
            freq[f].append(n)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


# hashmap = {}

# for num in nums:
#     if num in hashmap:
#         hashmap[num] += 1
#     else:
#         hashmap[num] = 1
        
# while len(hashmap) > k:

#     min_key = min(hashmap, key=hashmap.get)
#     del hashmap[min_key]

 # return list(hashmap.keys())
        