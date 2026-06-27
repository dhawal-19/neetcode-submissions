class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        h1,h2 = {},{}
        for val in s:
            h1[val] = h1.get(val,0) + 1
        for val in t:
            h2[val] = h2.get(val,0) + 1
        return h1 == h2