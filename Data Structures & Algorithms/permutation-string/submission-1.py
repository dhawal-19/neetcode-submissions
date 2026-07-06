from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = Counter(s1)
        i,j = 0,len(s1) - 1
        while j < len(s2):
            s2freq = Counter(s2[i:j+1])
            if s1freq == s2freq: return True
            i += 1
            j += 1
        return False
        