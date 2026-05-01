class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        i = 0
        hm = set()
        for j in range(len(s)):
            while s[j] in hm:
                hm.remove(s[i])
                i += 1
            hm.add(s[j])
            count = max(count, j - i + 1)
        return count