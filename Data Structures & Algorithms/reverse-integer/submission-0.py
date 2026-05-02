class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        isNeg = True if x < 0 else False
        x = abs(x)
        while x:
            rev = (rev * 10) + x % 10
            x = x // 10
        if isNeg:
            rev *= -1
        if rev in range(-2**31,2**31): return rev
        return 0
