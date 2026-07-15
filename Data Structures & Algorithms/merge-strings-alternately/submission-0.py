class Solution:
    def mergeAlternately(self, s: str, t: str) -> str:
        result = ""
        i,j,m,n = 0,0,len(s),len(t)
        while i < m and j < n:
            result += s[i]
            result += t[j]
            i += 1
            j += 1
        while i < m:
            result += s[i]
            i += 1
        while j < n:
            result += t[j]
            j += 1
        return result