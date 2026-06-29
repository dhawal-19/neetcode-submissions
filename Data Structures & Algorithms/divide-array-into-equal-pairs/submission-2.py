class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hm = set()
        for num in nums:
            if num in hm:
                hm.remove(num)
            else:
                hm.add(num)
        return len(hm) == 0