class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        ans = []
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in hm:
                hm[sorted_str].append(str)
            else:
                hm[sorted_str] = [str]
        for k,v in hm.items():
            ans.append(hm[k])
        return ans