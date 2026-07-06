class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = defaultdict(list)
        for i,v in enumerate(nums):
            hm[v].append(i)
        for indices in hm.values():
            if len(indices) < 2: continue
            for i in range(1,len(indices)):
                absval = abs(indices[i] - indices[i-1])
                if  absval <= k:
                    return True 
        return False