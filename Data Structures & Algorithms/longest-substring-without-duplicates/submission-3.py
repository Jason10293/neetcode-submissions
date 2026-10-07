class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        right = 0
        contains = set()
        while right < len(s):
            while right < len(s) and s[right] not in contains:
                contains.add(s[right])
                right += 1
                ans = max(ans, right - left)
            while left < len(s) and right < len(s) and s[right] in contains:
                contains.discard(s[left])
                left += 1
            
        return ans

                