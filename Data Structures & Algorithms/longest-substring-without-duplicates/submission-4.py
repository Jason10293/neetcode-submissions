class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        contains = set()
        for right, c in enumerate(s):
            while c in contains:
                contains.discard(s[left])
                left += 1
            contains.add(c)
            ans = max(ans, right - left + 1)
            
        return ans

                