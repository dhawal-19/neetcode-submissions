from bisect import bisect_left
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(1,len(nums) + 1):
            idx = bisect_left(nums,x)
            count = len(nums) - idx 
            if count == x:
                return x
        return -1
