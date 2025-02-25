class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str = ""
        if str1 + str2 != str2 + str1:
            return str

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        gcd_length = gcd(len(str1), len(str2))

        return str1[:gcd_length]

sol = Solution()
print(sol.gcdOfStrings(str1="abb", str2="abbabb"))