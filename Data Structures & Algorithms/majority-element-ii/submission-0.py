class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num,0) + 1
        ans = []
        threshold = len(nums) // 3
        for k,v in hm.items():
            if v > threshold:
                ans.append(k)
        return ans