class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        h1,h2 = {},{}
        for cnt in range(0,len(s)):
            h1[s[cnt]] = h1.get(s[cnt],0) + 1 
            h2[t[cnt]] = h2.get(t[cnt],0) + 1 
        return h1 == h2