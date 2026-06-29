class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num,0) + 1
        for values in hm.values():
            if values % 2 != 0:
                return False
        return True