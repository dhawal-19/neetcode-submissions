class Solution:
    def gcdOfStrings(self, a: str, b: str) -> str:
        if a + b != b + a: return ""
        gcd = math.gcd(len(a),len(b))
        return a[:gcd]