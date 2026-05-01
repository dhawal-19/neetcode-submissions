class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        ans = []
        for i in range(min(len(first),len(last))):
            fc = first[i]
            lc = last[i]
    
            if fc == lc:
                ans.append(fc)
            else:
                break   
        return ''.join(ans)