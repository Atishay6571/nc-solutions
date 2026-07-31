class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a,b =len(str1), len(str2)
        gcd = math.gcd(a,b)
        if str1+str2!= str2+str1:
            return ""
        return str1[:gcd]