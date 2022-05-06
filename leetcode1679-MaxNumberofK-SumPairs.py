class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash_map = {}
        for each in nums:
            if each in hash_map: hash_map[each] += 1
            else: hash_map[each] = 1
        n = 0
        for key in hash_map:
            try:
                if hash_map[k-key]>=hash_map[key] and (k-key)!=key:
                    val = hash_map[key]
                    hash_map[k-key] -= val
                    hash_map[key] -= val
                elif hash_map[k-key]>=hash_map[key]:
                    val= hash_map[key]//2
                else:
                    val = hash_map[k-key]
                    hash_map[k-key] -= val
                    hash_map[key] -= val
                n += val
            except KeyError: pass
        return n
