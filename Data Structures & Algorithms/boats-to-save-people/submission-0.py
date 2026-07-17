class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        i,j = 0, len(p) - 1
        minboats = 0
        while i <= j:
            if p[i] + p[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            minboats += 1        
        return minboats
