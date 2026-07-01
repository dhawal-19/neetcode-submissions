import bisect
from bisect import bisect_left
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        lo,hi = 0,n 
        while lo < hi:
            mid = (lo + hi + 1) // 2
            cnt = n - bisect_left(nums,mid)
            if cnt >= mid:
                lo = mid 
            else:
                hi = mid - 1
        cnt = n - bisect_left(nums,lo)
        return lo if cnt == lo else -1


