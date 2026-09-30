class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        shortest = ""
        if len(strs[0]) <= len(strs[-1]):
            shortest = strs[0]
        else:
            shortest = strs[-1]
        
        ans = ""
        for index, letter in enumerate(shortest):
            if strs[0][index] != strs[-1][index]:
                break
            ans += letter
        
        return ans