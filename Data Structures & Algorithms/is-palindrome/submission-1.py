class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for c in s.strip():
            if c.isalpha() or c.isdigit():
                ns += c
        ns = ns.lower()
        i,j = 0,len(ns) - 1
        while i < j:
            if ns[i] != ns[j]:
                return False
            i += 1
            j -= 1
        return True