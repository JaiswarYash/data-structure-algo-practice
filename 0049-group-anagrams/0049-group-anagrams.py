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