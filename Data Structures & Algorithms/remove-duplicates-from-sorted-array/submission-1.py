class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1
        for r in range(n):
            if nums[r] != nums[l - 1]:
                nums[l] = nums[r]
                l += 1
        return l

