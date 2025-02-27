class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_vowels = []
        s_list = list(s)
        for i in s:
            if i in vowels:
                s_vowels.append(i)
        vowels_reversed = s_vowels[::-1]
        counter = 0
        for i in s:
            if i in vowels:
                s_list[counter] = vowels_reversed[0]
                vowels_reversed.pop(0)
            else:
                s_list[counter] = i
            counter += 1
        return "".join(s_list)

sol = Solution()
print(sol.reverseVowels("leetcode"))