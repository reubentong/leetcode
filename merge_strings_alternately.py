class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        length = min(len(word1), len(word2))
        for i in range(length):
            merged += word1[i] + word2[i]
        return merged + word1[length:] + word2[length:]


sol = Solution()
print(sol.mergeAlternately(word1="reuben", word2="amna"))