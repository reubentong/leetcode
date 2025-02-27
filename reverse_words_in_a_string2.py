class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s)
        w = []
        word = ""
        for i in l:
            if i.isalnum():
                word += i
            elif word != "":
                w.append(word)
                word = ""
        if word.isalnum():
            w.append(word)
        w.reverse()
        return " ".join(w)

sol = Solution()
print(sol.reverseWords("EPY2giL"))