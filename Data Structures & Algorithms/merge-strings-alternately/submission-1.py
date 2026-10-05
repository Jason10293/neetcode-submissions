class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        ans = ""
        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1
        
        if i != len(word1) - 1:
            ans += "".join(word2[j:])
        if j != len(word2) - 1:
            ans += "".join(word1[i:])
            print(i, "", j)
        return ans