class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            val = nums[i]
            if target - val in hm:
                return [hm[target - val],i]
            hm[val] = i
        return []